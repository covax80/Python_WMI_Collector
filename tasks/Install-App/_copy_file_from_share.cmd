
@echo off

cd ..\..

rem python Z_current.py -H %1 -U %2 -C "Install 1C App" -X run_file_from_share -M plaintable2

rem python Z_current.py -H VOSTOK-WS040 -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M plaintable2

rem python Z_current.py -H "khab-ws238" -U "Admin" -P "AdminPass" -C "Install 1C App" -X run_file -M plaintable2

rem python Z_current.py -l "lll-3.txt" -U Admin -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F out.html

rem python Z_current.py -l "lll-4.txt" -U Admin -P "AdminPass" -C "Install 1C App" -X run_file -M html2 -F out.html

python Z_current.py -H "KHAB-WS090" -U Admin -P "AdminPass" -C "Install App" -X run_file3 -M plain

