DRIVE_TYPES = {
  0 : "Unknown",
  1 : "No Root Directory",
  2 : "Removable Disk",
  3 : "Local Disk",
  4 : "Network Drive",
  5 : "Compact Disc",
  6 : "RAM Disk"
}

c = wmi.WMI ()
for drive in c.Win32_LogicalDisk ():
  print drive.Caption, DRIVE_TYPES[drive.DriveType]