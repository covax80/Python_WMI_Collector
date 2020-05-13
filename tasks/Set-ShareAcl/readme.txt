$acl = Get-Acl `
  \\WH0RCUTEACHER\c$\Users\jxg768\Desktop\RobsShare
$permission = "OMEGA\JXL812","FullControl","Allow"
$accessRule = New-Object `
  System.Security.AccessControl.FileSystemAccessRule `
  $permission
$acl.SetAccessRule($accessRule)
$acl |
  Set-Acl \\WH0RCUTEACHER\c$\Users\jxg768\Desktop\RobsShare