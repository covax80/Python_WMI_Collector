#!python3


def show_share(con, command_line_arg,host):
	result = []
	for share in con.Win32_Share():
 		result.append([share.Name, share.Path])	
	return result
