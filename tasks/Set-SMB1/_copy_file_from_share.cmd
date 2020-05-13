
@echo off

cd ..\..

rem python Z_current.py -H %1 -U %2 -C "Install 1C App" -X run_file_from_share -M plaintable2

rem python Z_current.py -H VOSTOK-WS040 -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M plaintable2

rem python Z_current.py -H "khab-ws238" -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M plaintable2

rem python Z_current.py -l "lll-3.txt" -U Admin -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F out.html

rem python Z_current.py -l "lll-4.txt" -U Admin -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F out.html

rem python Z_current.py -l "D:\SVN\GUZHKH\Python_WMI_collector\tasks\Install-App1C\list.txt" -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F out222.html

rem python Z_current.py -l "D:\SVN\GUZHKH\Python_WMI_collector\tasks\Set-SMB1\list2.txt" -U "Admin" -P "AdminPass" -C "Remove SMB-1" -X smb1remove -M html2 -F 20190412-2-smb-1.html
python Z_current.py -H OFFICE-WS003 -U "Admin" -P "AdminPass" -C "Remove SMB-1" -X smb1remove -M html2 -F 20190412-smb-1.html

