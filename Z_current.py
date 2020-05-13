#!python3
# -*- coding: cp1251 -*-

#
#
#
#
# 



import win32con
import wmi

from datetime import datetime, timedelta
from pprint import pprint as pp
from pprint import pformat
from os import path as os_path
from time import time
from multiprocessing.dummy import Pool as ThreadPool
import sys
import re
import ipaddress
import importlib
import logging
import getpass
import traceback
import socket

from myutils import split_strip, tcpping, zfill_host, check_extra_zerro_in_ip4

#from configparser import ConfigParser

path = os_path.dirname(os_path.abspath(__file__))

#----------< CONFIG >----------------------
from optparse import OptionParser
parser = OptionParser(add_help_option=False)

from configparser import ConfigParser
config = ConfigParser()
config.read(path + '/settings.ini')

#--------------------------------------------

logger = logging.getLogger('just_do_wmit')
header = logging.FileHandler(datetime.now().strftime("%Y%m%d%H%M") +'_just_do_wmit.log')
logger.setLevel(getattr(logging, config.get('MAIN','logging_level',fallback='DEBUG')))
#debug(), info(), warning(), error() and critical().
logger.addHandler(header)

#Global variables
program_mode = 'HOSTMODE' # or "LISTMODE" or "RANGEMODE"
final_result = {}
command_line_arg = None
save_error = None

def process_config():
	global program_mode
	parser.add_option("-H", "--host", dest="host", 
			help="Host for connection", metavar="HOST", default=None)

	parser.add_option("-R", "--ip-range", dest="ip_range", 
			help="Ip range (Example: -R 172.21.72.0/24)", metavar="IP4RANG", default=None)

	parser.add_option("-L", "--host-list", dest="host_list", 
			help="Host list (Example: -L WORKSTATION-01.domain.local,WORKSTATION-02.domain.local)", 
			metavar="HOSTLIST", default=None)
	parser.add_option("-l", "--host-txt-list", dest="host_txt_list", 
			help="Import host list from text file (Example: -l buh_users.txt)", 
			metavar="HOSTLIST", default=None)

	parser.add_option("-U", "--user", dest="user", 
			help="UserName for WMI Credential", metavar="USER", default=None)

	parser.add_option("-P", "--password", dest="password", 
			help="Password for WMI Credential", metavar="PASSWD", default=None)

	parser.add_option("-C", "--command", dest="command", 
			help="WMI Command (Example: -C \"Select * From Win32_SerialPort\" )", metavar="CMD", default=None)

	parser.add_option("-X", "--extract_rule", dest="extract_rule", 
			help="Input plugin name for postprocessing from \"processors\" folder (Example:get_C_disk_freespace)", metavar="XRULE", default="plain_text")
	
	parser.add_option("-M", "--mode", dest="save_mode", 
			help="Choice save file format: plain,plain2,plaintable,plaintable2,html,html2,csv,csv2", metavar="SAVEMODE", default='plain')

	parser.add_option("-A", "--wmi-object-properties", dest="wmi_object_properties", 
			help="get list of the wmi object properties", metavar="PROPRTIES", default=None)

	parser.add_option("-F", "--file-name", dest="filename", 
			help="Input file name for saving", metavar="FILE", default=None)

	parser.add_option("-G", "--header", dest="result_header", 
			help="Header for output result", metavar="HEADER", default=None)
	                                                                                	

	parser.add_option("-N", "--namespace", dest="namespace", 
			help="WMI namespace", metavar="NAMESPACE", default="root\\cimv2")


	parser.add_option("-?", "--help", dest="help", 
			help="Get HELP", default=None)




	args = None
	global command_line_arg
	(command_line_arg, args) = parser.parse_args(args)

	if sum([int(bool(x)) for x in [command_line_arg.host,command_line_arg.ip_range,
		command_line_arg.host_list,command_line_arg.host_txt_list]]) > 1:
		print("Error: Not compatable options: -H,-R,-l and -L. Need only one of them")
		sys.exit(1)


	if not command_line_arg.filename and \
	       command_line_arg.save_mode not in ['plain','plain2','plaintable','plaintable2']:
		print('ERROR: Need to fill --file-name option')
		exit(2)


	
	if command_line_arg.ip_range:
		program_mode = 'RANGEMODE'
		command_line_arg.host_list = ",".join([str(ipaddr) for ipaddr in ipaddress.IPv4Network(command_line_arg.ip_range)])
		command_line_arg.host_list = split_strip(command_line_arg.host_list)
	elif (command_line_arg.host_list or command_line_arg.host_txt_list):
		program_mode = 'LISTMODE'
		if command_line_arg.host_txt_list:
			with open(command_line_arg.host_txt_list) as hosts_list_file:
				command_line_arg.host_list = ",".join(hosts_list_file.readlines())
		command_line_arg.host_list = split_strip(command_line_arg.host_list)
		command_line_arg.host_list = check_extra_zerro_in_ip4(command_line_arg.host_list)
	else:
		program_mode = 'HOSTMODE'
	
	logger.info('program mode is "%s"'%program_mode)


	if command_line_arg.user and not command_line_arg.password:
		command_line_arg.password = getpass.getpass(prompt='Password: ', stream=None)

	if command_line_arg.result_header:
		command_line_arg.result_header = split_strip(command_line_arg.result_header)
		#command_line_arg.result_header = [x.encode('utf-8').decode('cp1251') for x in command_line_arg.result_header]
	"""if not command_line_arg.command or \
		bool(command_line_arg.help) == True or \
		sum([int(bool(x)) for x in [command_line_arg.host,command_line_arg.ip_range,
		command_line_arg.host_list,command_line_arg.host_txt_list]]) < 1:
		"""
	if not command_line_arg.command or bool(command_line_arg.help) == True:
		parser.print_help()
		exit(0)
	

	#pp(command_line_arg)
	logger.debug("Command line options\n%s"%pformat(command_line_arg))
	return
                                   

def get_WMI_object(host):
	"""Запрашиваем из WMI _object_ через WQL"""	
	global save_error

	#pp(command_line_arg)
	"""if not command_line_arg.user:
		obj = wmi.WMI(host, moniker=command_line_arg.command)	
	else:
		obj = wmi.WMI(host, user=command_line_arg.user, password=command_line_arg.password, moniker=command_line_arg.command)
	"""
	con = None
        		
	try:
		if not command_line_arg.user:
			con = wmi.WMI(host, namespace=command_line_arg.namespace)
		else:   	
			logger.info("wmi.WMI(host=%(host)s, user=%(user)s, password=%(password)s"%{'host':host, 'user':command_line_arg.user, 'password':command_line_arg.password})		
			con = wmi.WMI(host, namespace=command_line_arg.namespace, user=command_line_arg.user, password=command_line_arg.password)
			#c.Win32_ComputerSystem.methods.keys()
	
		logger.info("Request :\t%s"%command_line_arg.command)
		

		if command_line_arg.command.upper().startswith('SELECT'):
			wql = command_line_arg.command		
			obj = con.query(wql)
		else:
			obj = con
	except Exception as err:
		save_error = str(err).replace("<","").replace(">","")
		return False
	return obj

def process_one_host(host):
	global save_error
	"""После получения объекта WMI 
		1. смотрим каким post-processor-ом его обработать
		2. если post-processor-a нет, то возращем просто текстовой выриант ответа - максимально его распотрошив
		3. из post-processor-a данные должны выйти в виде таблицы для их дальнейшей записи в формате:
			[ [cell_1_1,cell_1_2.cell_1_3], [cell_2_1,cell_2_2,cell_2_3],... ]                   
	"""
	"""if not tcpping(host):
		save_error = "NO RESPONSE"
		result = False	
		logger.debug("HOST %s unreachable or Port 135 close"%host)
	else:	"""

	result = get_WMI_object(host)

	if result:
		process = importlib.import_module('processors')
		process = getattr(process,command_line_arg.extract_rule)
		#print(">>>",dir(process))
		result = process(result,command_line_arg,host)
	else:
		try:
			result = [[socket.gethostbyaddr(host)[0],save_error]]
		except:
			result = [['ERROR',save_error]]
	#print(">>>>")
	#pp(result)
	return result
	
		

#def process_multi_hosts(hosts_list):
	
	

             	

def process_hosts():
	global final_result, save_error
        
	if program_mode == 'HOSTMODE':
		#pp(command_line_arg)
		if not command_line_arg.host:
			command_line_arg.host = 'localhost'
		final_result[command_line_arg.host] = process_one_host(command_line_arg.host)
		logger.debug(pformat(final_result))
	else:
		logger.debug("Process_hosts: %s"%pformat(command_line_arg.host_list))
		
		pool = ThreadPool(128)		
		ping_all_hosts  = pool.map(tcpping,command_line_arg.host_list)
		new_host_list = []
		i = 0
		for host_availible in ping_all_hosts:
			logger.debug("HOST %s reachable  - %s "%(command_line_arg.host_list[i],str(host_availible)))
			if host_availible:
				new_host_list.append(command_line_arg.host_list[i])		
			i += 1  
               
		command_line_arg.host_list = new_host_list

		for host in command_line_arg.host_list:
			save_error = None
			logger.debug("REQUEST TO:\t%s\t%s"%(host,pformat(command_line_arg.command)))
			final_result[host] = process_one_host(host)
			logger.debug("RESPONSE FROM:\t%s\n%s"%(host,pformat(final_result[host])))
	
	logger.debug("*final_result - %s "%(final_result))
	                               		
                              
def save_result(result):
	
	#raw_table = make_table()

	if '2' in command_line_arg.save_mode:
		command_line_arg.save_mode = command_line_arg.save_mode.replace("2","")
		

	if command_line_arg.save_mode == 'plain':
		import csv		
		f = open('.\\tmp_file','w', newline='')	
		with f as csvfile:
			rec = csv.writer(csvfile,dialect='excel',delimiter=' ')
			rec.writerows(result)
		print(open('.\\tmp_file').read())
		

	elif command_line_arg.save_mode == 'plaintable':		
		import output_func
		logger.debug(pformat(result))
		res = output_func.print_table(result)
		print(res)

	elif command_line_arg.save_mode == 'csv':
		import csv		
		f = open(command_line_arg.filename,'w', newline='')	
		with f as csvfile:
			rec = csv.writer(csvfile,dialect='excel',delimiter=';')
			rec.writerows(result)
		
	elif command_line_arg.save_mode == 'html':
		import output_func		
		logger.debug("BEFORE:\t%s"%pformat(result))
		data = output_func.html_table(result,"Date :%s"%datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
		logger.debug("AFTER:\t%s"%pformat(data))
		data = data.encode('cp1251','replace').decode('cp1251','replace')
		open(command_line_arg.filename,'w').write(data)
	else:
		print("Error: Unknown option \"-M\" SAVE MODE")
		sys.exit(1)
	return 



def save():
	global final_result
	result = []
	tmp = None
        
	for host in final_result.keys():
		tmp = []		
		for row in final_result[host]:
			if row == None:
				row = ['Unknown error', '' ]
			elif type(row) == str:
				row = ['Unknown error', row]
			if '2' in command_line_arg.save_mode:				
				row.insert(0,zfill_host(host))
			tmp.append(row)	
			print(tmp)

			final_result[host] = tmp
		result += final_result[host]
        
	if command_line_arg.result_header:
		result.insert(0, command_line_arg.result_header )
	
	logger.debug("RESULT:\t%s"%pformat(result))
	save_result(result)
             	


def main():
#	try:
	s_time = time()

	if 1:
	

		process_config()
		process_hosts()
		save()
#	finally:
#		logger.critical("ERROR") 

	logger.info("Finished in %s sec." % str(time()-s_time)) 
	logger.info(str(datetime.now())) 
	return




if __name__ == '__main__':
	main()




