@echo off
cd ../..

rem cls

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2html -F invent%date%.all.html

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2html -F invent%date%.all2.html

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2csv -F invent%date%.all2.csv

rem python Z_current.py -H 10.0.78.60 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2html -F invent%date%.sergey.html

rem python Z_current.py -C "GET DATA" -G "User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M html -F invent%date%.ws60.html

rem python Z_current.py -H OFFICE-WS011 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2csv -F invent%date%.OFFICE-WS011.csv

rem python Z_current.py -H OFFICE-WS001 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2csv -F invent%date%.OFFICE-WS001.csv

python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "GET DATA" -G "IP,User,OS,WS_name,PC_model,PC_serial,MAC,Monitor_model,Monitor_serial,Printer_model,Scanner_model,Web-cam_Model" -X inventer -M 2csv -F invent%date%.all.csv

