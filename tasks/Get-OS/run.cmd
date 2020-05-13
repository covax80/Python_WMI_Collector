cls

@echo off

cd ..\..


rem python Z_current.py -H %1 -U "Admin" -P "AdminPass" -C "SELECT CSName, Caption FROM Win32_OperatingSystem"  -A "CSName,Caption" -M plaintable
rem python Z_current.py -H %1 -U "Admin" -P "AdminPass" -C "SELECT CSName, Caption FROM Win32_OperatingSystem" -M plaintable

rem python Z_current.py -H %1 -U "Admin" -P "AdminPass" -C "SELECT Name FROM Win32_OperatingSystem" -M html2 -F os-report-%date%.html

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "SELECT CSName,Caption FROM Win32_OperatingSystem"  -A "CSName,Caption" -G "Рабочая станция,Операционная система"  -M html -F os-report-%date%.html
python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "SELECT CSName,Caption FROM Win32_OperatingSystem"  -A "CSName,Caption" -G "Рабочая станция,Операционная система"  -M csv -F os-report-%date%.csv

rem python Z_current.py -l list01.txt -U Admin -P "R@k2H@lj$$17" -C "SELECT Name FROM Win32_OperatingSystem" -M plaintable2

rem python Z_current.py -H OFFICE-WS095 -U "Admin" -P "AdminPass" -C "SELECT CSName,Caption FROM Win32_OperatingSystem"  -M csv -F os-report-%date%h95.csv


