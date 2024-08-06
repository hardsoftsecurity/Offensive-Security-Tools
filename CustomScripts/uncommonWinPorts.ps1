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

# Mostrar los puertos y marcar los inusuales
$portsListening | ForEach-Object {
    $port = $_.LocalPort
    $info = $_
    if ($commonPorts -contains $port) {
        Write-Output "$info"
    } else {
        Write-Output "$info --> X (Inusual)"
    }
}
