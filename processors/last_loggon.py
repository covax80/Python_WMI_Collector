#!python3

import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)) + sep + pardir)

from myutils import netcopydir, split_strip
import datetime
import wmi


def windowsDateConversion(string):
	res = datetime.datetime.strptime(string.split(".")[0],"%Y%m%d%H%M%S") + datetime.timedelta(hours=10)
	return res.strftime("%H:%M %d.%m.%Y")
	


def last_loggon(con, command_line_arg, host = 'TEST-WS000'):

	rec_limit = 1	
	#print(rec_limit)	
	if command_line_arg.wmi_object_properties:
		rec_limit = split_strip(command_line_arg.wmi_object_properties)
		if str(rec_limit[0]).isdigit():
			rec_limit = int(rec_limit[0])

		
	#con = wmi.WMI(privileges=["Security"])
	result = []
	lastLogin = None
	try:
		events = con.Win32_NTLogEvent(["InsertionStrings","TimeGenerated"],EventCode=4624)[0:rec_limit]    # For Win XP et 2k, EventCode = 680, but with Vista EventCode = 4624
		for lastLoginLog in events:
			lastLogin = [lastLoginLog.InsertionStrings[1],lastLoginLog.TimeGenerated]
			# convert the date
			lastLogin[1] = windowsDateConversion(lastLogin[1])
			result.append(lastLogin)
		
	except (WindowsError, wmi.x_wmi, IndexError): # pyflakes.ignore
		result = [["Error","N/A"]]

	return result




if __name__ == '__main__':
	import wmi
	host 		= "172.21.72.153"

	class	EmptyClass:
		pass
 	
	command_line_arg 		= EmptyClass()
	command_line_arg.user 		= "Admin"
	command_line_arg.password 	= "AdminPass"	#input("Enter password: ")
	command_line_arg.namespace	= "root\\cimv2"
	command_line_arg.wmi_object_properties = "10"

	con=wmi.WMI(	host, namespace = command_line_arg.namespace, 
			user=command_line_arg.user, password=command_line_arg.password )

	print(last_loggon(con, command_line_arg, host))
	
	
           
