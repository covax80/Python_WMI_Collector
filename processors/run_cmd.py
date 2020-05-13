#!python3


import wmi

import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)) + sep + pardir)


def run_cmd(con, command_line_arg, host = 'OFFICE-WS095'):
	print(command_line_arg.command)
	
	tmp_result = []
	
	try:
		process_id, return_value = con.Win32_Process.Create(CommandLine = command_line_arg.command )
	except AttributeError as exc:
		return  [["ERROR",str(exc)]]
		
	for process in con.Win32_Process(ProcessId = process_id):
		tmp_result = "Created processID: %s \nProcessName: %s"%(str(process.ProcessId), process.CommandLine)
 	
	#3. Return result of installation
	return  [["CMD STARTED",tmp_result]]
            






if __name__ == '__main__':

	from ad_user import local_admin, local_admin_passwd
	from sys import argv

	class	EmptyClass:
		pass       
 	
	command_line_arg 		= EmptyClass()
	command_line_arg.user 		= local_admin
	command_line_arg.password 	= local_admin_passwd
	command_line_arg.namespace	= "root\\cimv2"
	command_line_arg.command 	= "cmd.exe /c \"echo 1\""

	host = "OFFICE-WS095" 

	if len(argv) > 2:
		host 			 = argv[1]
		command_line_arg.command = argv[2]


	con=wmi.WMI(	host, namespace = command_line_arg.namespace, 
			user=command_line_arg.user, password=command_line_arg.password )

	print(run_cmd(con, command_line_arg, host))
	
	
           
