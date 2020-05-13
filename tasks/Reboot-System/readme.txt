import wmi
c = wmi.WMI ()
for opsys in c.Win32_OperatingSystem ():
  break

print opsys.Reboot
print opsys.Shutdown


$server = gwmi win32_operatingsystem 
$server.reboot() 