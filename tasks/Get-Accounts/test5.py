# -*- coding: cp1251 -*-
import win32con
import wmi

from sys import argv



def run(*args):
	print(locals())
	host,user,passwd = args
	c = wmi.WMI(host,user=user,password=passwd)
	for user in c.Win32_Account(["Caption", "Description","SID"]):
		sid = user.SID.split("-")
		if len(sid) > 4:
			if len(sid[4]) > 5:	
				print(user.Caption)
				print(user.Description)
    

if __name__ == '__main__':
      run(argv[1],argv[2],argv[3])
 
