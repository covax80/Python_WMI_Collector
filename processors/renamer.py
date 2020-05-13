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



def renamer(con, command_line_arg, host = 'TEST-WS000'):
	
	src_dir = "D:\\SCAN\\DISTR\\WS"
	dst_dir	= "C:\\Distr\\WS"	
	exec_file = "renamer-2.bat"
	create_bat = "netdom renamecomputer %%COMPUTERNAME%% /newname:DST_NAME /force \nrmdir /S /Q %(dst_dir)s"%locals()

	if not (os.path.exists(src_dir + "\\" + "renamer.bat")):
		mkdir(src_dir)
		time.sleep(1)
		open(src_dir  + "\\" + "renamer.bat","w").write(create_bat)

	dst_host_list = str(command_line_arg.command).split(",")
	host_index = get_src_host_index(command_line_arg, host)	
	dst_host = get_dst_host(dst_host_list, host_index)
                    
	#------------------------------
	bat_file = open(src_dir + "\\" + "renamer.bat","r").read()
	open(src_dir + "\\" + exec_file,"w").write(bat_file.replace("DST_NAME",dst_host))


	#run_setup_file = "cmd.exe /c " + dst_dir + "\\" + exec_file
	run_setup_file = dst_dir + "\\" + exec_file
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
	
	print("\n\nRENAME %(host)s ->  %(dst_host)s\n\n"%locals())
	return  [["INSTALLATION START",tmp_result]]
                		
	print(locals())

	

                                                                                                              


def get_src_host_index(command_line_arg, host):
	# if only one host rename
	if command_line_arg.host:
		return 0
	print("Host index = %d"%command_line_arg.host_list.index(host))
	return command_line_arg.host_list.index(host)



def get_dst_host(dst_host_list, host_index):
	# command_line_arg.command have a list new name for workstation with delimiter ","
	# if host in host_list have index 1 - then and in command_line_arg.command index 1 too
	# # python Z_current.py -L "KOMS-WS030,KOMS-WS020" -U Admin -P "AdminPass" -C "HOST-WS017,HOST-WS018" -X renamer -M plain
	# command_line_arg.host_list[1] = command_line_arg.command[1]
	# KOMS-WS020 will renamed to HOST-WS018
	print("dst_host_list[%d] = %s"%(host_index, dst_host_list[host_index]))
	return dst_host_list[host_index]

            
            






if __name__ == '__main__':
	# python Z_current.py -L "KOMS-WS030,KOMS-WS020" -U sl_admin -P "AdminPass" -C "OFFICE5-WS017,OFFICE5-WS018" -X renamer -M plain
	host 		= "10.0.78.60"
	#host 		= None

	class	EmptyClass:
		pass
 	
	command_line_arg 		= EmptyClass()
	command_line_arg.user 		= "admin"
	command_line_arg.password 	= "AdminPass"	#input("Enter password: ")
	command_line_arg.namespace	= "root\\cimv2"
#	command_line_arg.host_list	=  ['10.0.78.0', '10.0.78.1', '10.0.78.2']
	#command_line_arg.host_list	=  ["10.0.78.60"]
	command_line_arg.command	= "OFFICE5-WS222"
	command_line_arg.host 		= host


	con=wmi.WMI(	host, namespace = command_line_arg.namespace, 
			user=command_line_arg.user, password=command_line_arg.password )

	print(renamer(con, command_line_arg, host))
	
	
           
