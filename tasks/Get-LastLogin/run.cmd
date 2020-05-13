
@echo off
cd ..\..
python Z_current.py -H %1 -U Admin -C "Get Time Last logon" -X last_loggon -M plaintable2