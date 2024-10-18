# Lista de puertos comunes en un sistema Windows
$commonPorts = @(
    21,  # FTP
    22,  # SSH
    23,  # Telnet
    25,  # SMTP
    53,  # DNS
    80,  # HTTP
    110, # POP3
    135, # RPC
    139, # NetBIOS
    143, # IMAP
    443, # HTTPS
    445, # SMB
    3389 # RDP
)

# Obtener la lista de puertos a la escucha
$portsListening = Get-NetTCPConnection -State Listen

# Mostrar los puertos y marcar los inusuales con solo propiedades necesarias, incluyendo el nombre del proceso
$portsListening | ForEach-Object {
    $port = $_.LocalPort
    $procId = $_.OwningProcess
    $processName = (Get-Process -Id $procId).ProcessName  # Obtener el nombre del proceso

    if ($commonPorts -contains $port) {
        Write-Output "Port: $($port), Process: $processName, Local Address: $($_.LocalAddress), Remote Address: $($_.RemoteAddress), State: $($_.State)"
    } else {
        Write-Output "Port: $($port), Process: $processName, Local Address: $($_.LocalAddress), Remote Address: $($_.RemoteAddress), State: $($_.State) --> X (Inusual)"
    }
}
