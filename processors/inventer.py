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



def inventer(con, command_line_arg, host = 'TEST-WS000'):
	

	#	User	OS	WS name		PC model	PC serial	MAC	Monitor model	Monitor serial	
	#	Printer model	Printer serial	Scanner model	Scanner serial	Web-cam Model	Web-cam serial


	def get_username():
		return con.Win32_ComputerSystem.query()[0].UserName

	def get_os():
		return con.Win32_OperatingSystem()[0].Caption
		
	def get_ws_name():
		return con.Win32_ComputerSystem.query()[0].Name

	def get_pc_model():
		return con.Win32_ComputerSystem.query()[0].Manufacturer + " " + con.Win32_ComputerSystem.query()[0].Model

	def get_pc_serial():
		return con.Win32_bios.query()[0].SerialNumber
				
	def get_pc_mac():
		for network_adapter in con.Win32_NetworkAdapter.query():
			if network_adapter.AdapterType and "Ethernet" in network_adapter.AdapterType:
				return network_adapter.MACAddress
		return ""

	def get_monitor_model():
		#con2 = wmi.WMI(host, namespace="root\\wmi")
		con2 = wmi.WMI(host, namespace="root\\wmi", user=command_line_arg.user, password=command_line_arg.password)
		res = con2.wmiMonitorID.query()[0]
		return tuple2str(res.ManufacturerName) + " " + tuple2str(res.UserFriendlyName)
						  
	def get_monitor_serial():
		con2 = wmi.WMI(host, namespace="root\\wmi", user=command_line_arg.user, password=command_line_arg.password)
		res = con2.wmiMonitorID.query()[0]
		return tuple2str(res.SerialNumberID)


	def get_printer_model():
		printer = con.Win32_Printer.query(Default = "TRUE")
		if not printer:
			return ""
		printer = printer[0]
	#	if "USB" in printer.PortName:
		if 1:
			return printer.DriverName

	def get_scanner_model():
		scanner = con.query("SELECT Manufacturer,Name FROM Win32_PnPEntity WHERE Caption LIKE '%scan%' AND PNPDeviceID LIKE '%USB\%'")
		if not scanner:
			return ""
		return scanner[0].Manufacturer + " " + scanner[0].Name


	def get_webcam_model():
		webcam = con.query("SELECT Manufacturer,Name FROM Win32_PnPEntity WHERE Caption LIKE '%cam%' AND PNPDeviceID LIKE '%USB\%'")
		if not webcam:
			return ""
		return webcam[0].Manufacturer + " " + webcam[0].Name


#	User	OS	WS name		PC model	PC serial	MAC	Monitor model	Monitor serial	
	#	Printer model	Printer serial	Scanner model	Scanner serial	Web-cam Model	Web-cam serial



	functions = [ 	get_username,
			get_os,
			get_ws_name,
			get_pc_model,
			get_pc_serial,
			get_pc_mac,
			get_monitor_model,
			get_monitor_serial,
			get_printer_model,
			get_scanner_model,
			get_webcam_model ]

	result = []

	for func in functions:
		try:
			result.append( func() )
		
		except Exception as ex:
      			result.append( str(ex) )

	return  [ result ]

	 

#tst = (76, 68, 81, 48, 67, 4, 9, 56, 50, 52, 48, 74, 53, 0, 0, 0, 0)


def tuple2str(data):
	return "".join([chr(x) for x in data if x > 0])

        


if __name__ == '__main__':
	host 		= "10.0.78.60"
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
	#con=wmi.WMI(	host, namespace = command_line_arg.namespace, user=command_line_arg.user, password=command_line_arg.password )
	con=wmi.WMI()
	print(inventer(con, command_line_arg, host))
	
	                                                                   	
           
