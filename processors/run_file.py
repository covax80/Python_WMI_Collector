#!python3

import datetime 
import time
import wmi

import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)) + sep + pardir)

from myutils import netcopydir




def run_file(con, command_line_arg, host = 'TEST-WS000'):
	
	#0. Define variables
	#src_dir = "D:\\SCAN\\DISTR\\1C_8.3.7.2027"
	#dst_dir	= "C:\\Distr\\1C\\1C_8.3.7.2027"
	#run_setup_file = "cmd.exe /c C:\\Distr\\1C\\1C_8.3.7.2027\\setup.exe /S"
	#src_dir = "D:\\SCAN\\DISTR\\1C_8.3.9.1818"
	#src_dir = "D:\\SCAN\\DISTR\\1C_8.3.10.2466"
	#src_dir = "D:\\SCAN\\DISTR\\1C_8.3.10.2561"
	src_dir = "D:\\SCAN\\DISTR\\1C_8.3.12.1790"
	#src_dir = "D:\\SCAN\\DISTR\\1C_8.3.16.1063"
	#src_dir = "D:\\SCAN\\DISTR\\1C_8.3.9.2033_32"	
	#dst_dir	= "C:\\Distr\\1C\\1C_8.3.9.2033_32"	
	#dst_dir	= "C:\\Distr\\1C\\1C_8.3.9.1818"	
	dst_dir	= "C:\\Distr\\1C\\1C_8.3.12.1790"
	#dst_dir	= "C:\\Distr\\1C\\1C_8.3.16.1063"
	#------------------------------
	#run_setup_file = "cmd.exe /c C:\\Distr\\1C\\1C_8.3.16.1063\\setup.exe /S"
	run_setup_file = "cmd.exe /c C:\\Distr\\1C\\1C_8.3.12.1790\\setup.exe /S"
	tmp_result = ""
	result = []
	
	#1. COPY Distr to targer host	
	netcopydir(host, src_dir, dst_dir, username=command_line_arg.user, password=command_line_arg.password)


	#2. RUN setup file	
	try:
		process_id, return_value = con.Win32_Process.Create(CommandLine = run_setup_file)
	except AttributeError as exc:
		return  [["ERROR",str(exc)]]
		
	for process in con.Win32_Process(ProcessId = process_id):
		tmp_result += "Created processID: %s ProcessName: %s\n"%(str(process.ProcessId), process.Name)
 	
	#3. Return result of installation
	return  [["INSTALLATION START",tmp_result]]


	


	#src_dir = "D:\\SVN\\GUZHKH\\Python_WMI_collector\\processors\\svn"
	
	#try:
	
		#netcopy(host, src_dir, dst_dir, username=command_line_arg.user, password=command_line_arg.password)
	"""
	except Exception as err:
		if isinstance(err, win32wnet.error) and err[0] == 1326:
			return (["ERROR","The process of distr. files coping is failed"])
	"""               
	print(locals())

	#return ["",""]

	#result.append(["job_ID / result", str(job_id) + "/" + str(run_result)])







                   
            
            






if __name__ == '__main__':
	host 		= "10.0.78.74"

	class	EmptyClass:
		pass
 	
	command_line_arg 		= EmptyClass()
	command_line_arg.user 		= "Admin"
	command_line_arg.password 	= "AdminPass"	#input("Enter password: ")
	command_line_arg.namespace	= "root\\cimv2"

	con=wmi.WMI(	host, namespace = command_line_arg.namespace, 
			user=command_line_arg.user, password=command_line_arg.password )

	print(run_file(con, command_line_arg, host))
	
	
           

