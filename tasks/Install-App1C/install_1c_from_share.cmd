
@echo off

cd ..\..

rem python Z_current.py -H %1 -U %2 -C "Install 1C App" -X run_file_from_share -M plaintable2

rem python Z_current.py -H VOSTOK-WS040 -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M plaintable2

rem python Z_current.py -H "khab-ws238" -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M plaintable2

rem python Z_current.py -l "lll-3.txt" -U Admin -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F out.html

rem python Z_current.py -l "lll-4.txt" -U Admin -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F out.html

rem python Z_current.py -l "D:\SVN\GUZHKH\Python_WMI_collector\tasks\Install-App1C\list.txt" -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F out222.html

rem python Z_current.py -l "D:\SVN\GUZHKH\Python_WMI_collector\tasks\Install-App1C\list4.txt" -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F install1c2019.html
rem python Z_current.py -H OFFICE-WS033 -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F install1c2019stot.html

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F 202022_install_1c_8.3.18.html

python Z_current.py -H 10.0.78.141 -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F 20200213_install_1c_8.3.16.html


