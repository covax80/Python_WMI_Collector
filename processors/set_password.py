#!python3

import wmi
import win32com.client
import pythoncom
from pywintypes import com_error as pywintypes_com_error
#import pywintypes

import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)) + sep + pardir)



def set_password(con, command_line_arg, host):
	args = command_line_arg.command.split(',')
	if len(args) > 2:
		args = [args[0], args[2], args[1]]
	else:
		args = [args[0], None, args[1]]
	account,old_passwd,new_passwd = args
	#adsi_ns = win32com.client.Dispatch('ADsNameSpaces')
	#adsi_request = f"WinNT://{host}/{account},user"
	#print(adsi_request)
	#account = adsi_ns.GetObject(adsi_request)
	try:
		account = win32com.client.GetObject(f"WinNT://{host}/{account},user")
	except pywintypes_com_error as exc:
		return  [["ERROR", str(exc)]]				
	try:
		if old_passwd:
			account.ChangePassword(old_passwd, new_passwd)
		else:
			account.SetPassword(new_passwd)	
		# set additional attribs : PASS_NOT_EXPIRIED && NORMAL_ACCOUNT && PASSWORD_CANT_CHANGE
		#admin.userflags = 66112	
		#admin.SetInfo()
	except pywintypes_com_error as error_details:		
		hr, msg, exc, arg = error_details.args
		scode = exc[5]
		err = "NT Password change has failed."
		if scode == 0x8007005:
			err = "Your NT Account (%s) is locked out."%args[0]
		elif scode == 0x80070056:
			err = "Invalid Old NT Password."
		elif scode == 0x800708ad:
			err = "The specified NT Account (%s) does not exist."%args[0]
		elif scode == 0x800708c5:
			err = "Your new password cannot be the same as any of your previous passwords, and must satisfy the domain's password-uniqueness policies."
		else:
        	    err = "ADSI Error - %x: %s, %x" % (hr, msg, scode)
		
		return  [["ERROR", err]]

	return [["OK","NT Password change was successful."]]





if __name__ == '__main__':

	from ad_user import *
	from sys import argv

	class EmptyClass:pass

	command_line_arg 		= EmptyClass()
	command_line_arg.command 	= "admin,1234567890"
	command_line_arg.user 		= "DOMAIN\\" + admin
	command_line_arg.password 	= admin_passwd
	command_line_arg.namespace	= r"root\cimv2"

	#con = None
	host = 'WS127'
	if len(argv) > 2:
		host 			 = argv[1]
		command_line_arg.command = argv[2]

	#con = wmi.WMI('WS127', namespace = r"root\cimv2" , user='DOMAIN\\, password=command_line_arg.password )
	con=wmi.WMI( host, namespace = command_line_arg.namespace, user=command_line_arg.user, password=command_line_arg.password )

	print(set_password(con, command_line_arg, host))
	
                                                     

                                                
