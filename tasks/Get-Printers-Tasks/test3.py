#!python3

import wmi

from sys import argv

def wmi_connection(server, username, password):
        print("attempting connection with", server)
        if username:
            return wmi.WMI(server, user=username, password=password)
        else:
            return wmi.WMI(server)

"""servers = [
       (".", "", ""),
       ("goyle", "wmiuser", "secret")
    ]"""

def get_printer_job(server, username=None, password=None):
    watchers = {}
    #for server, username, password in servers:
    connection = wmi_connection(server, username, password)
    watchers[server] = connection.Win32_PrintJob.watch_for("creation")

    while True:
        for server, watcher in watchers.items():
            try:
                event = watcher(timeout_ms=10)
            except(wmi.x_wmi_timed_out):
                pass
            else:
                print("print job added on", server)
                print(event.Name)
                print(event.Owner,">> ",event.Document,event.TotalPages)


if __name__ == '__main__':
    if len(argv) > 2:
	       get_printer_job(argv[1],argv[2],argv[3])
    else:
            get_printer_job(argv[1])

