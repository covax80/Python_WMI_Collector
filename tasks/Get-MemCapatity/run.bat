cls

@echo off

cd ..\..


rem python Z_current.py -H %1 -U ".\Admin" -P "AdminPass" -C "SELECT Capacity FROM Win32_PhysicalMemory" -G * -M csv2 -F mem_capacity.csv

rem python Z_current.py -R 172.28.0.0/23 -U ".\Admin" -P "AdminPass" -C "SELECT Capacity FROM Win32_PhysicalMemory" -G * -M csv2 -F mem_capacity.csv

python Z_current.py -l ws_list.txt -U ".\Admin" -P "AdminPass" -C "SELECT Capacity FROM Win32_PhysicalMemory" -G * -M csv2 -F mem_capacity.csv

