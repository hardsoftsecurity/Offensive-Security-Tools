# Offensive Security Tools Collection

This repository contains a collection of binaries and tools that I have utilized during my OSCP (Offensive Security Certified Professional) certification and various Capture The Flag (CTF) challenges. These tools are essential for tasks such as penetration testing, privilege escalation, exploitation, and post-exploitation.

## Tools List

### Custom Scripts

| Rate | Name                  | Description                              | GitHub Link                              |
|------|-----------------------|------------------------------------------|------------------------------------------|
| 7    | checkDisabledFunc.php | A PHP script to check for disabled functions in PHP environments | [checkDisabledFunc.php](https://github.com/hax3xploit/EZ-Tmux/blob/main/tmux.conf) |
| 6    | uncommonWinPorts.ps1  | A script to identify uncommon open ports on Windows | [uncommonWinPorts.ps1](https://github.com/hax3xploit/EZ-Tmux/blob/main/tmux.conf) |

### Enumeration

| Rate | Name           | Description                                      | GitHub Link                            |
|------|----------------|--------------------------------------------------|----------------------------------------|
| 8    | dirsearch      | A simple command line tool designed to brute force directories and files in web servers | [dirsearch](https://github.com/maurosoria/dirsearch) |
| 9    | linpeas.sh     | A script that searches for possible paths to escalate privileges on Linux/Unix systems | [linpeas](https://github.com/carlospolop/PEASS-ng) |
| 9    | nmap.exe       | A network scanning tool for discovering hosts and services on a computer network | [nmap](https://github.com/nmap/nmap) |
| 9    | nmap.zip       | A network scanning tool for discovering hosts and services on a computer network | [nmap](https://github.com/nmap/nmap) |
| 9    | nmap_linux     | A network scanning tool for discovering hosts and services on a computer network | [nmap](https://github.com/nmap/nmap) |
| 8    | pspy64         | A tool to monitor Linux processes without root permissions | [pspy](https://github.com/DominicBreuker/pspy) |
| 8    | winPEAS.bat    | A batch script to check for common misconfigurations and vulnerabilities for Windows privilege escalation | [winPEAS](https://github.com/carlospolop/PEASS-ng) |
| 8    | winPEASx64.exe | The 64-bit version of winPEAS for Windows privilege escalation | [winPEAS](https://github.com/carlospolop/PEASS-ng) |

### Miscellaneous

| Rate | Name          | Description                                           | GitHub Link                              |
|------|---------------|-------------------------------------------------------|------------------------------------------|
| 6    | directoryLists| A collection of directory listings used for web application fuzzing | [directoryLists](https://github.com/danielmiessler/SecLists) |
| 7    | gdb_commands  | A collection of GDB commands and scripts for debugging | [gdb_commands](https://github.com/cyrus-and/gdb-dashboard) |
| 8    | git-dumper    | A tool to dump a git repository from a website         | [git-dumper](https://github.com/arthaud/git-dumper) |
| 7    | ntlm_theft    | Tools for capturing NTLM hashes                        | [ntlm_theft](https://github.com/fox-it/mitm6) |
| 7    | passwordList  | A collection of commonly used passwords for brute-force attacks | [passwordList](https://github.com/danielmiessler/SecLists) |

### Pivoting

| Rate | Name            | Description                                          | GitHub Link                          |
|------|-----------------|------------------------------------------------------|--------------------------------------|
| 8    | chisel          | A fast TCP tunnel, transported over HTTP, secured via SSH | [chisel](https://github.com/jpillora/chisel) |
| 7    | ligolo-agent    | Ligolo is a simple, lightweight, and fast reverse-tunneling tool optimized for penetration testers | [ligolo](https://github.com/sysdream/ligolo-ng) |
| 7    | ligolo-agent.exe| Windows version of the Ligolo agent                  | [ligolo](https://github.com/sysdream/ligolo-ng) |
| 7    | ligolo-proxy    | Proxy component for Ligolo reverse tunneling         | [ligolo](https://github.com/sysdream/ligolo-ng) |
| 8    | plink.exe       | PuTTY Link: a command-line connection tool similar to SSH | [plink](https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe) |
| 8    | socat           | A relay for bidirectional data transfer between two independent data channels | [socat](http://www.dest-unreach.org/socat/) |
| 8    | socat.zip       | A relay for bidirectional data transfer between two independent data channels | [socat](http://www.dest-unreach.org/socat/) |

### Post-Exploitation

| Rate | Name                 | Description                                              | GitHub Link                         |
|------|----------------------|----------------------------------------------------------|-------------------------------------|
| 8    | DecryptAutoLogon.exe | Tool used to decrypt saved credentials for auto logon    | [DecryptAutoLogon](https://github.com/HarmJ0y/ASREPRoast) |
| 9    | Invoke-Mimikatz.ps1  | A PowerShell script to run the famous Mimikatz tool for credential dumping | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| 8    | PowerUp.ps1          | A PowerShell script for privilege escalation on Windows machines | [PowerUp](https://github.com/HarmJ0y/PowerUp) |
| 7    | PrivescCheck.ps1     | A PowerShell script to enumerate possible paths to escalate privileges on a Windows machine | [PrivescCheck](https://github.com/itm4n/PrivescCheck) |
| 8    | Rubeus.exe           | A tool for Kerberos abuse, including ticket requests and renewals | [Rubeus](https://github.com/GhostPack/Rubeus) |
| 7    | RunasCs.exe          | A tool for executing commands with different user privileges | [RunasCs](https://github.com/ropnop/kerbrute) |
| 7    | RunasCs.zip          | A tool for executing commands with different user privileges | [RunasCs](https://github.com/ropnop/kerbrute) |
| 7    | RunasCs_net2.exe     | Another variant of RunasCs for specific .NET environments | [RunasCs](https://github.com/ropnop/kerbrute) |
| 8    | Seatbelt.exe         | A C# project that performs a number of security-related checks on a Windows system | [Seatbelt](https://github.com/GhostPack/Seatbelt) |
| 9    | SharpHound.exe       | A tool for gathering Active Directory information for BloodHound | [SharpHound](https://github.com/BloodHoundAD/SharpHound3) |
| 9    | SharpHound.ps1       | A PowerShell script for gathering Active Directory information for BloodHound | [SharpHound](https://github.com/BloodHoundAD/SharpHound3) |
| 9    | mimikatz.exe         | A tool for dumping credentials from Windows systems      | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| 9    | mimikatz64.exe       | The 64-bit version of Mimikatz                           | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| 8    | mimikatz_trunk       | The development branch of Mimikatz with the latest features | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| 8    | mimikatz_trunk.zip   | The development branch of Mimikatz with the latest features | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| 8    | pypykatz             | A Python implementation of Mimikatz to extract credentials from memory dumps | [pypykatz](https://github.com/skelsec/pypykatz) |
| 7    | unix-privesc-check   | A script to check for common misconfigurations and vulnerabilities for Unix privilege escalation | [unix-privesc-check](https://github.com/pentestmonkey/unix-privesc-check) |

### Reverse Shells

| Rate | Name                 | Description                                              | GitHub Link                           |
|------|----------------------|----------------------------------------------------------|---------------------------------------|
| 8    | PowerShellGenerators | A collection of PowerShell scripts for various offensive tasks | [PowerShellGenerators](https://github.com/samratashok/nishang) |
| 8    | nc                   | Netcat, a versatile networking tool                       | [nc](https://github.com/diegocr/netcat) |
| 8    | nc.exe               | The Windows version of Netcat                            | [nc](https://github.com/diegocr/netcat) |
| 8    | nc64.exe             | The 64-bit version of Netcat for Windows                 | [nc](https://github.com/diegocr/netcat) |
| 8    | pentestmonkey        | A collection of pentesting scripts                        | [pentestmonkey](https://github.com/pentestmonkey/scripts) |
| 7    | powercat.ps1         | A PowerShell TCP/IP Swiss army knife, a tool for network interactions | [powercat](https://github.com/besimorhino/powercat) |

### Token Exploitation

| Rate | Name                 | Description                                              | GitHub Link                             |
|------|----------------------|----------------------------------------------------------|-----------------------------------------|
| 8    | GodPotato-NET4.exe   | A privilege escalation tool exploiting COM services      | [GodPotato](https://github.com/BeichenDream/GodPotato) |
| 8    | JuicyPotato.exe      | A privilege escalation tool for Windows exploiting the token duplication vulnerability | [JuicyPotato](https://github.com/ohpe/juicy-potato) |
| 8    | JuicyPotatoNG.exe    | An updated version of JuicyPotato for Windows privilege escalation | [JuicyPotatoNG](https://github.com/antonioCoco/JuicyPotatoNG) |
| 8    | JuicyPotatoNG.zip    | An updated version of JuicyPotato for Windows privilege escalation | [JuicyPotatoNG](https://github.com/antonioCoco/JuicyPotatoNG) |
| 8    | PrintSpoofer64.exe   | A tool for privilege escalation using the Print Spooler service | [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) |
| 8    | SharpEfsPotato.exe   | A tool for exploiting Windows EFS to gain privileges     | [SharpEfsPotato](https://github.com/CCob/SweetPotato) |
| 8    | SweetPotato.exe      | Another privilege escalation tool similar to JuicyPotato | [SweetPotato](https://github.com/CCob/SweetPotato) |

### Tools

| Rate | Name           | Description                                      | GitHub Link                             |
|------|----------------|--------------------------------------------------|-----------------------------------------|
| 9    | CrackMapExec   | A Swiss army knife for pentesting Windows/Active Directory environments | [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) |
| 9    | evil-winrm     | The ultimate WinRM shell for hacking/pentesting  | [evil-winrm](https://github.com/Hackplayers/evil-winrm) |
| 9    | impacket       | A collection of Python classes for working with network protocols | [impacket](https://github.com/SecureAuthCorp/impacket) |
| 8    | joomscan       | A vulnerability scanner for Joomla CMS           | [joomscan](https://github.com/OWASP/joomscan) |
| 8    | kerbrute_linux_amd64 | A tool to quickly brute force and enumerate valid Active Directory accounts | [kerbrute](https://github.com/ropnop/kerbrute) |
| 8    | kr             | A tool for remote command execution via SSH      | [kr](https://github.com/kryptco/kr) |
| 9    | powerview.ps1  | A PowerShell tool to gain network situational awareness on Windows domains | [PowerView](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1) |

## Usage

To use any of these tools, simply navigate to the appropriate directory and execute the binary or script. Ensure that you have the necessary permissions and environment set up for each tool to function correctly.

## Acknowledgements

This configuration was inspired by various tools and configurations available online. Special thanks to the offensive security community for their contributions and shared knowledge.

---

Feel free to contribute to this repository by opening issues or submitting pull requests with improvements and suggestions.
