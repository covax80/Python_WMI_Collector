(Get-WmiObject -Namespace Root\OpenHardwareMonitor -Class sensor | Where-Object {$_.SensorType -eq 'Temperature'} | Where-Object {$_.Name -eq 'CPU Core #1'}).Value