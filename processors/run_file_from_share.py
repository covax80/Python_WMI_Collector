#!python3

import datetime 
import time
import wmi

import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)) + sep + pardir)

from myutils import netcopy


#netcopy(host, source, dest_dir, username=None, password=None, move=False):
                
def run_file_from_share(con, command_line_arg, host = 'TEST-WS000'):
	result = []
	start_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
	share_name 	= "\\\\VOSTOK-WS060\\Scan"
	user		= "VOSTOK-WS060\\ShareAcc"
	passwd		= "SharePass"
	distr_dir	= "Distr\\1C_8.3.7.2027"
	log_dir		= "Distr\\LOG"
	prog_name	= "setup.exe /S"
	command_1  = "net use %(share_name)s /USER:%(user)s %(passwd)s"%locals()
	command_2  = "%(share_name)s\\%(distr_dir)s\\%(prog_name)s"%locals()	
	log_file   = "%(share_name)s\\%(log_dir)s\\"%locals() + \
					datetime.datetime.now().strftime("%Y%m%d%H%M") + "__" + host + "_log.txt"

	source_file   	= "D:\\SCAN\\DISTR\\CMD\\1c.ps1"
	dest_dir	= "C:\\Users\\Public\\Documents"

	netcopy(host, source_file, dest_dir, command_line_arg.user, command_line_arg.password)	
	time.sleep(5)

	job_id, run_result = con.Win32_ScheduledJob.Create( 
			 	Command		= "cmd /c C:\\Users\\Public\\Documents\\1c.ps1",
				StartTime	= wmi.from_time( 
							year=start_time.year,
							month=start_time.month,
							day=start_time.day,
							hours=start_time.hour,
							minutes=start_time.minute,
							seconds=start_time.second,
							microseconds=0,timezone=600))


	#Command		= "cmd.exe /c \"%(command_1)s ; %(command_2)s > %(log_file)s\""%locals(),
	result.append(["job_ID / result", str(job_id) + "/" + str(run_result)])
	print("[%s] job: %s created" %(host,str(job_id)))	
	return result
           