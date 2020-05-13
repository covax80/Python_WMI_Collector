cls

@echo off

cd ..\..

rem python Z_current.py -H %1 -U sl_admin -C "SELECT Name,Path FROM c.Win32_Share" -M plaintable2


rem --------Show all shares on localhost
rem python Z_current.py -C "Show me all Shares" -X show_share -M plaintable2
    
rem python Z_current.py -H %1 -U %2 -C "Show me all Shares" -X show_share -M plaintable2

rem python Z_current.py -H OFFICE-WS001 -U Admin -P "AdminPass" -C "Show me all Shares" -X show_share -M plaintable2

rem python Z_current.py -H %1 -U Admin -P "AdminPass" -C "Show me all Shares" -X show_share -M plaintable2

rem python Z_current.py -l %1 -U Admin -P "AdminPass" -C "Show me all Shares" -X show_share -M plaintable2

python Z_current.py -R 10.0.78.0/23 -U Admin -P "AdminPass" -C "Show me all Shares" -X show_share -M csv2 -F all_share.csv

python Z_current.py -l list01.txt -U Admin -P "AdminPass" -C "Show me all Shares" -X show_share -M csv2 -F all_share3.csv



