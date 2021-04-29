@echo off

cd ..\..


python Z_current.py  -R 172.28.40.0/24 -C "admin,SomePass" -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_10.csv 
python Z_current.py  -R 172.28.36.0/24 -C "admin,SomePass" -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_9.csv 
python Z_current.py  -R 172.28.32.0/24 -C "admin,SomePass" -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_8.csv 
python Z_current.py  -R 172.28.28.0/24 -C "admin,SomePass" -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_7.csv 
python Z_current.py  -R 172.28.24.0/24 -C "admin,SomePass" -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_6.csv 
python Z_current.py  -R 172.28.20.0/24 -C "admin,SomePass" -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_5.csv 
python Z_current.py  -R 172.28.16.0/24 -C "admin,SomePass" -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_4.csv 
python Z_current.py  -R 172.28.12.0/24 -C "admin,SomePass" -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_3.csv 
python Z_current.py  -R 172.28.8.0/24 -C "admin,SomePass"  -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_2.csv 
python Z_current.py  -R 172.28.4.0/24 -C "admin,SomePass"  -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_district_1.csv

rem python Z_current.py  -H WS127 -C "admin,SomePass"  -X set_password -M plaintable2

rem python Z_current.py  -R 172.28.0.0/23 -C "admin,SomePass"  -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass.csv

 

rem python Z_current.py  -l ws_list.txt -C "admin,SomePass"  -G "Host,Status,Message" -X set_password -M csv2 -F set_new_pass_20210412.csv

rem python Z_current.py  -R 172.28.1.0/24 -C "admin,SomePass"  -X set_password -M html -F set_new_pass_20210412.html

rem #python Z_current.py -l ws_list.txt -C "admin,NewPassword" -X set_password -M html2 -F set_new_pass.html

rem #python Z_current.py -l ws_list.txt -C "admin,OldPassword,NewPassword" -X set_password -M plain > set_new_pass.log