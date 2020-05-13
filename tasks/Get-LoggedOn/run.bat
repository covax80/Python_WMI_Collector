
cd ..\..

rem python Z_current.py -C "Select * from Win32_ComputerSystem"  -H "Paramter,UserName" -M html2 -F logged%date%.html
rem python Z_current.py -C "Select * from Win32_ComputerSystem" -G "Host,Property,Value" -M html2 -F logged%date%.html

rem python Z_current.py -H %1 -U Admin -C "Select * from Win32_ComputerSystem" -M plaintable2
rem --------Show all shares on localhost                                                        
rem python Z_current.py -H %1 -U %2 -C "Select * from Win32_ComputerSystem"  -M plaintable2
python Z_current.py -H %1 -U Admin -C "Select * from Win32_ComputerSystem" -M plaintable2




