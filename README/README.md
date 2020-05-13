# BASIC WMI CLASSES


```
Example:
con = wmi.WMI(namespace="root\\cimv2")
res = con.query("SELECT * FROM Win32_Processor")

res[0].proprties.keys()
```
                       

--------------------------------------------------------------------
Win32_BaseBoard
       Motherboard
Win32_Fan
	System fan
Win32_Keyboard
	Keyboard
Win32_PointingDevice
	The pointing device, such as a mouse
Win32_CDROMDrive
	CD-ROM
Win32_DiskDrive
	The system's hard drive
Win32_PhysicalMedia
	Any storage device, in general machine, including CD-ROM, a physical hard disk, floppy disk, tape machine etc.
Win32_BIOS
	System BIOS
Win32_CacheMemory
	The system Cache memory
Win32_MemoryDevice
	Memory address, mapping with associated
Win32_PhysicalMemory
	Physical memory
Win32_Processor
	CPU
Win32_NetworkAdapter
	The network adapter, including physical card
Win32_NetworkAdapterConfiguration
	The network adapter configuration
Win32_NetworkAdapterSetting
	The network adapter and its related settings
Win32_Printer
	Printer / fax device
Win32_DesktopMonitor
	Display device
Win32_DisplayConfiguration
	Display device configuration
Win32_Desktop
	Desktop
Win32_Environment
	System environment
Win32_Directory
	File directory, all directory
Win32_DiskPartition
	The disk partition
Win32_LogicalDisk
	The logical disk
Win32_Process
	Process information
Win32_Account
	Account information
Win32_PerfFormattedData
	Performance data formatted
Win32_Service
	System service