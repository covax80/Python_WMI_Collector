#!python3

import socket
import sys
import os
from os import listdir, path as os_path, remove as os_remove
from os.path import dirname, realpath, sep, pardir

import shutil
import win32wnet
import getpass
from optparse import OptionParser



def split_strip(comma_separated_txt="", delimiter=","):
	return [x.strip() for x in comma_separated_txt.split(delimiter)]


def tcpping(host = "127.0.0.1", port = 135, tcp_timeout = 1):
	rs=True
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(tcp_timeout)
	try:
		s.connect((host,port))
		s.close()
	except socket.timeout:
		rs=False
	except socket.error:
		rs=False
	except:
		rs=False
		print("INFO:",str(sys.exc_info()))
	return rs



def zfill_host(host):
	if host.count(".") != 3:
		return host
	tmp = [int(x) for x in split_strip(comma_separated_txt=host, delimiter=".")]
	return "%.3d.%.3d.%.3d.%.3d"%tuple(tmp)




def netcopydir(host, source, dest_dir, username=None, password=None):
	#if not os_path.isdir(source):
	#	netcopy(host, source, dest_dir, username, password)
	for lists in listdir(source):

		path 		= os_path.join(source, lists)
		dest_path = str(sep).join((os_path.join(dest_dir, lists)).split(sep)[:-1])

		if not os_path.isdir(path):		
			netcopy(host, path, dest_path, username, password)
			print(path,"\t->\t",dest_path)	        		
		else:
			netcopydir(host, path, dest_path, username, password)
	

	return



def netcopy(host, source, dest_dir, username=None, password=None, move=False):
    """ Copies files or directories to a remote computer. """
    
    wnet_connect(host, username, password)
            
    dest_dir = covert_unc(host, dest_dir)

    # Pad a backslash to the destination directory if not provided.
    if not dest_dir[len(dest_dir) - 1] == '\\':
        dest_dir = ''.join([dest_dir, '\\'])

    # Create the destination dir if its not there.
    if not os_path.exists(dest_dir):
        os.makedirs(dest_dir)
    else:
        # Create a directory anyway if file exists so as to raise an error.
         if not os_path.isdir(dest_dir):
             os.makedirs(dest_dir)

    if move:
        shutil.move(source, dest_dir)
    else:
        try:
            shutil.copy(source, dest_dir)
	
        except PermissionError:
            pass







def netdelete(host, path, username=None, password=None):
    """ Deletes files or directories on a remote computer. """
    
    wnet_connect(host, username, password)

    path = covert_unc(host, path)
    if os_path.exists(path):
        # Delete directory tree if object is a directory.        
        if os_path.isfile(path):
            os_remove(path)
        else:
            shutil.rmtree(path)
    else:
        # Remove anyway if non-existent so as to raise an error.        
        os_remove(path)

def netmove(host, source, dest_dir, username=None, password=None):
    return netcopy(host, source, dest_dir, username, password, True)


def covert_unc(host, path):
    """ Convert a file path on a host to a UNC path."""
    return ''.join(['\\\\', host, '\\', path.replace(':', '$')])

    
def wnet_connect(host, username, password):
	unc = ''.join(['\\\\', host])
	#print(str(unc))
	try:
		win32wnet.WNetAddConnection2(0, None, unc, None, username, password)
	except Exception as err:
		if isinstance(err, win32wnet.error):
		# Disconnect previous connections if detected, and reconnect.
			try:
				if err[0] == 1219:
					win32wnet.WNetCancelConnection2(unc, 0, 0)
					return wnet_connect(host, username, password)
			except:
				pass
		raise err





def check_extra_zerro_in_ip4(ip4_list):
	new_ip4_list = []
	tmp = []
	for ip4 in ip4_list:
		if ip4.count(".") == 3:
			for x in ip4.split("."):
				if x.isdigit():
					tmp.append(x)
				else:
					new_ip4_list.append(ip4)
					break
			if len(tmp) == 4:
				new_ip4_list.append(".".join([str(int(y)) for y in tmp]))
				tmp = []
		else:
			new_ip4_list.append(ip4)
	return new_ip4_list
	




