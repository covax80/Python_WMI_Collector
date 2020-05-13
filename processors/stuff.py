from wmi import wmi

con = wmi.WMI()

wmic = con.Win32_bios


def all3(wmic):
	for k in wmic.properties.keys():
		print(k + ": " + str(getattr(wmic,k).value))


def all2(wmic):
	for k in wmic.properties.keys():
		print(k + ": " + str(getattr(wmic,k)))


def all(wmic):
	for k,v in wmic.properties.items():
		print(k + ": " + str(getattr(wmic,k).value))