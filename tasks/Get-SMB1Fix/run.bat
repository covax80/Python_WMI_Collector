
cd ..\..


rem python Z_current.py -H %1 -U "Admin" -P "AdminPass" -C "SELECT CSName,HotFixID,Description,InstalledOn,InstalledBy FROM Win32_QuickFixEngineering WHERE HotFixID LIKE '%%4012212%%'" -G "CSName,HotFixID,Description,InstalledOn,InstalledBy" -M plaintable2

rem python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass" -C "SELECT CSName,HotFixID,Description,InstalledOn,InstalledBy FROM Win32_QuickFixEngineering WHERE HotFixID LIKE '%%4012212%%'" -M "csv2" -F "smb1fix%date%.csv"

rem python Z_current.py -H "OFFICE-WS095" -U "Admin" -P "AdminPass"  -C "SELECT CSName,HotFixID FROM Win32_QuickFixEngineering WHERE HotFixID LIKE '%%4012212%%'" -A "CSName,HotFixID" -M "csv2" -F "smb1fix%date%.csv"

rem python Z_current.py -H "OFFICE-WS066" -U "Admin" -P "AdminPass"  -C "SELECT CSName,HotFixID FROM Win32_QuickFixEngineering WHERE HotFixID LIKE '%%4012212%%'" -A "CSName,HotFixID" 

python Z_current.py -R 10.0.78.0/23 -U "Admin" -P "AdminPass"  -C "SELECT CSName,HotFixID FROM Win32_QuickFixEngineering WHERE HotFixID LIKE '%%KB3133977%%'" -A "CSName,HotFixID" -M "csv2" -F "sha2%date%.csv"






