#!python3

import datetime 
import time
import wmi

import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)) + sep + pardir)

from myutils import netcopydir
from os import system,mkdir
import os



def smb1remove(con, command_line_arg, host = 'TEST-WS000'):
	
	src_dir = "D:\\SCAN\\DISTR\\SMB1"
	dst_dir	= "C:\\Distr\\SMB1"	
	exec_file = "WannaCryDefenderLocal.bat"
	msu_file = "Win7-kb4012212-x64.msu "
	                  
	#------------------------------
	
	#run_setup_file = "cmd.exe /c " + dst_dir + "\\" + exec_file
	run_bat_file = dst_dir + "\\" + exec_file
	run_msu_file = dst_dir + "\\" + exec_file
	tmp_result = ""
	result = []
	
	#1. COPY Distr to targer host	
	netcopydir(host, src_dir, dst_dir, username=command_line_arg.user, password=command_line_arg.password)

	#2. RUN bat file	
	try:
		process1_id, return_value1 = con.Win32_Process.Create(CommandLine = run_bat_file)		
	except AttributeError as exc:
		return  [["ERROR",str(exc)]]
		
	#2. MSU bat file	
	try:
		process2_id, return_value2 = con.Win32_Process.Create(CommandLine = run_msu_file)		
		#print(return_value2)
	except AttributeError as exc:
		return  [["ERROR",str(exc)]]


	for process in con.Win32_Process(ProcessId = process1_id):
		tmp_result += "RUN bat file %s with process ID: %s\n"%(process.Name,str(process.ProcessId))

	for process in con.Win32_Process(ProcessId = process2_id):
		tmp_result += "RUN msu file %s with process ID: %s\n"%(process.Name,str(process.ProcessId))
 	
	#3. Return result of installation   

	return  [["PATCH START",tmp_result]]              		




if __name__ == '__main__':
	host 		= "KHAB-WS041"

	#host 		= None

	class	EmptyClass:
		pass
 	
	command_line_arg 		= EmptyClass()
	command_line_arg.user 		= "Admin"
	command_line_arg.password 	= "AdminPass"	#input("Enter password: ")
	command_line_arg.namespace	= "root\\cimv2"
#	command_line_arg.host_list	=  ['10.0.78.0', '10.0.78.1', '10.0.78.2']
	#command_line_arg.host_list	=  ["10.0.78.60"]
	command_line_arg.command	= host
	command_line_arg.host 		= host


	con=wmi.WMI(	host, namespace = command_line_arg.namespace, 
			user=command_line_arg.user, password=command_line_arg.password )

	print(smb1remove(con, command_line_arg, host))
	
	
           
