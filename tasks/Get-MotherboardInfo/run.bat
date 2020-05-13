
cd ..\..

rem python Z_current.py -C "Select * from Win32_ComputerSystem"  -H "Paramter,UserName" -M html2 -F logged%date%.html
rem python Z_current.py -C "Select * from Win32_ComputerSystem" -G "Host,Property,Value" -M html2 -F logged%date%.html

rem python Z_current.py -H %1 -U Admin -C "Select * from Win32_ComputerSystem" -M plaintable2
rem --------Show all shares on localhost                                                        
rem python Z_current.py -H %1 -U %2 -C "Select * from Win32_ComputerSystem"  -M plaintable2
rem python Z_current.py -   -C "Install 1C App" -X run_file -M html2 -F out333.html

rem python Z_current.py -H %1 -U "Admin" -P "AdminPass" -C "SELECT * FROM Win32_BaseBoard" -A "Name,Manufacturer,Product,Description," -M plaintable2

rem python Z_current.py -H %1 -U "Admin" -P "AdminPass" -C "SELECT * FROM Win32_BaseBoard" -A "Manufacturer,Product" -M plaintable2

python Z_current.py -H %1 -U "Admin" -P "AdminPass" -C "SELECT Manufacturer,Product FROM Win32_BaseBoard" -G "a,Manufacturer,Product" -M plaintable2

rem 'Caption', 'ConfigOptions', 'CreationClassName', 'Depth', 'Description', 'Height', 'HostingBoard', 'HotSwappable', 
rem 'InstallDate', 'Manufacturer', 'Model', 'Name', 'OtherIdentifyingInfo', 'PartNumber', 'PoweredOn', 'Product', 'Removable',
rem  'Replaceable', 'RequirementsDescription', 'RequiresDaughterBoard', 'SerialNumber', 'SKU', 'SlotLayout', 
rem 'SpecialRequirements', 'Status', 'Tag', 'Version', 'Weight', 'Width'




