@echo off
cd ../..
rem cls

rem python Z_current.py -l lll-2.txt -U "sl_admin" -C "Select Name,UserName from Win32_ComputerSystem" -A UserName -G "Host,Param,Value" -M csv2 -F all%date%.ws-2.csv

rem python Z_current.py -R 172.21.72.0/24 -U "Admin" -P "AdminPass" -C "Select Name,UserName from Win32_ComputerSystem" -A UserName -G "Host,Param,Value" -M csv2 -F all%date%.ws172.csv
rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "" -C "Select Name,UserName from Win32_ComputerSystem" -A UserName -G "Host,Param,Value" -M csv2 -F all%date%.ws10.csv
rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "Select Name,UserName from Win32_ComputerSystem" -A UserName -G "Host,Param,Value" -M csv2 -F all%date%.ws11.csv
rem python Z_current.py -C "Select Name,UserName from Win32_ComputerSystem" -A UserName -G "Host,Param,Value" -M plaintable

rem python Z_current.py -R 172.21.72.0/24 -U "UserAcc" -C "Select UserName from Win32_ComputerSystem" -A UserName -G "Host,Param,Value" -M csv2 -F all%date%.ws.csv

python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "Select Name,UserName from Win32_ComputerSystem" -A UserName -G "Host,Param,Value" -M csv2 -F all%date%.ws.csv

