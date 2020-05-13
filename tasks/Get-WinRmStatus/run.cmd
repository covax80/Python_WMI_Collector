cls

rem @echo off

cd ../..

rem python Z_current.py -H "OFFICE-WS095" -U "Admin" -P "AdminPass" -C "SELECT SystemName,Name,State FROM Win32_Service WHERE Name = 'WinRM'" -A "SystemName,Name,State" -G "АРМ,Служба,Статус" -M "csv" -F "winrm-report-%date%.csv" 

python Z_current.py -H "OFFICE-WS095" -U "Admin" -P "AdminPass" -C "SELECT SystemName,Name,State FROM Win32_Service WHERE Name = 'WinRM'" -A "SystemName,Name,State" -G "АРМ,Служба,Статус"

rem python Z_current.py -R "10.0.78.0/23" -U "Admin" -P "AdminPass" -C "SELECT SystemName,Name,State FROM Win32_Service WHERE Name = 'WinRM'" -A "SystemName,Name,State" -G "АРМ,Служба,Статус" -M "csv" -F "winrm-report-%date%-2.csv" 