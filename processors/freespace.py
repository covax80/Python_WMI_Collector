import wmi
import os


def freespace(con, command_line_arg, host = 'TEST-WS000'):
	result = []
	try:
		username = con.Win32_ComputerSystem.query()[0].UserName
		for disk in con.Win32_LogicalDisk():
			if disk.DriveType == 3:
				space = 100 * int(disk.FreeSpace) / int(disk.Size)
				#print( "%s has %d%% free" % (disk.Name, space))
				result.append( [username, disk.Caption, str(space)] )
	except Exception as ex:
		result = [str(ex),None,None]

	return  result 


if __name__ == '__main__':
	host 		= "10.0.78.74"
	class	EmptyClass:
		pass        	
	command_line_arg 		= EmptyClass()
	command_line_arg.user 		= "Admin"
	command_line_arg.password 	= "AdminPass"	#input("Enter password: ")
	command_line_arg.namespace	= "root\\cimv2"
#	command_line_arg.host_list	=  ['10.0.78.0', '10.0.78.1', '10.0.78.2']
	#command_line_arg.host_list	=  ["10.0.78.60"]
	command_line_arg.command	= "Get DATA"
	command_line_arg.host 		= host
	con=wmi.WMI(	host, namespace = command_line_arg.namespace, user=command_line_arg.user, password=command_line_arg.password )
	#con=wmi.WMI()
	print(freespace(con, command_line_arg, host))
	
	                                                                   	
