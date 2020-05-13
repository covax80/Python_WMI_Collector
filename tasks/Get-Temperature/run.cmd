
cls

@echo off

cd ..\..



rem python Z_current.py -R 10.0.78.0/24 -U "Admin" -P "AdminPass" -C "Select CurrentTemperature from MSAcpi_ThermalZoneTemperature" -A UserName -G "Host,Param,Value" -M csv2 -F all%date%.ws10.csv

rem python Z_current.py -H localhost -C "SELECT * FROM sensor WHERE sensortype = 'Temperature' AND Name = 'CPU Core #1'" --namespace "openhardwaremonitor" -A  "Host,Param,Value" -M plain

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "SELECT * FROM sensor WHERE sensortype = 'Temperature' AND Name = 'CPU Core #1'" --namespace "root\\openhardwaremonitor" -A  "Host,Param,Value" -M csv2 -F report.cpu.temp.%date%-2.csv

rem python Z_current.py -H KHAB-WS090 -U "Admin" -P "AdminPass" -C "SELECT * FROM sensor WHERE sensortype = 'Temperature' AND Name = 'CPU Core #1'" --namespace "root\\openhardwaremonitor" -A  "Host,Param,Value" -M csv2 -F report.cpu.temp.%date%-3.csv

python Z_current.py -H KHAB-WS090 -U "Admin" -P "AdminPass" -C "SELECT * FROM sensor WHERE sensortype = 'Temperature' AND Name = 'CPU Core #1'" --namespace "root\\openhardwaremonitor" -A  "Host,Param,Value" -M plain