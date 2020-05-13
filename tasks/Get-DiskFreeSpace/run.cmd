@echo off
cd ../..
rem cls


rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2html -F invent%date%.all.html

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2html -F invent%date%.all2.html

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2csv -F invent%date%.all2.csv

rem python Z_current.py -H 10.0.78.60 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2html -F invent%date%.sergey.html

rem python Z_current.py -C "GET DATA" -G "User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M html -F invent%date%.ws60.html

rem python Z_current.py -H 10.0.73.74 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,Disk,FreeSpace" -X freespace -M html2 -F freespace%date%2.html

rem python Z_current.py -l list01.txt -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,Account,Disk,FreeSpace" -X freespace -M html2 -F freespace%date%.html

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,Account,Disk,FreeSpace" -X freespace -M html2 -F freespace%date%-2.html

python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,Account,Disk,FreeSpace" -X freespace -M html2 -F freespace%date%

rem python Z_current.py -H OFFICE-WS056 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,Account,Disk,FreeSpace" -X freespace -M plaintable 

