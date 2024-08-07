# Offensive Security Tools Collection

This repository contains a collection of binaries and tools that I have utilized during my OSCP (Offensive Security Certified Professional) certification and various Capture The Flag (CTF) challenges. These tools are essential for tasks such as penetration testing, privilege escalation, exploitation, and post-exploitation.
- **The links to the tools are not updated.**


## Tools List

### Custom Scripts

| Name                  | Description                              | GitHub Link                              |
|-----------------------|------------------------------------------|------------------------------------------|
| checkDisabledFunc.php | A PHP script to check for disabled functions in PHP environments | [checkDisabledFunc.php](https://github.com/hax3xploit/EZ-Tmux/blob/main/tmux.conf) |
| uncommonWinPorts.ps1  | A script to identify uncommon open ports on Windows | [uncommonWinPorts.ps1](https://github.com/hax3xploit/EZ-Tmux/blob/main/tmux.conf) |

### Enumeration

| Name           | Description                                      | GitHub Link                            |
|----------------|--------------------------------------------------|----------------------------------------|
| dirsearch      | A simple command line tool designed to brute force directories and files in web servers | [dirsearch](https://github.com/maurosoria/dirsearch) |
| linpeas.sh     | A script that searches for possible paths to escalate privileges on Linux/Unix systems | [linpeas](https://github.com/carlospolop/PEASS-ng) |
| nmap.exe       | A network scanning tool for discovering hosts and services on a computer network | [nmap](https://github.com/nmap/nmap) |
| nmap.zip       | A network scanning tool for discovering hosts and services on a computer network | [nmap](https://github.com/nmap/nmap) |
| nmap_linux     | A network scanning tool for discovering hosts and services on a computer network | [nmap](https://github.com/nmap/nmap) |
| pspy64         | A tool to monitor Linux processes without root permissions | [pspy](https://github.com/DominicBreuker/pspy) |
| winPEAS.bat    | A batch script to check for common misconfigurations and vulnerabilities for Windows privilege escalation | [winPEAS](https://github.com/carlospolop/PEASS-ng) |
| winPEASx64.exe | The 64-bit version of winPEAS for Windows privilege escalation | [winPEAS](https://github.com/carlospolop/PEASS-ng) |

### Miscellaneous

| Name          | Description                                           | GitHub Link                              |
|---------------|-------------------------------------------------------|------------------------------------------|
| directoryLists| A collection of directory listings used for web application fuzzing | [directoryLists](https://github.com/danielmiessler/SecLists) |
| gdb_commands  | A collection of GDB commands and scripts for debugging | [gdb_commands](https://github.com/cyrus-and/gdb-dashboard) |
| git-dumper    | A tool to dump a git repository from a website         | [git-dumper](https://github.com/arthaud/git-dumper) |
| ntlm_theft    | Tools for capturing NTLM hashes                        | [ntlm_theft](https://github.com/fox-it/mitm6) |
| passwordList  | A collection of commonly used passwords for brute-force attacks | [passwordList](https://github.com/danielmiessler/SecLists) |

### Pivoting

| Name            | Description                                          | GitHub Link                          |
|-----------------|------------------------------------------------------|--------------------------------------|
| chisel          | A fast TCP tunnel, transported over HTTP, secured via SSH | [chisel](https://github.com/jpillora/chisel) |
| ligolo-agent    | Ligolo is a simple, lightweight, and fast reverse-tunneling tool optimized for penetration testers | [ligolo](https://github.com/sysdream/ligolo-ng) |
| ligolo-agent.exe| Windows version of the Ligolo agent                  | [ligolo](https://github.com/sysdream/ligolo-ng) |
| ligolo-proxy    | Proxy component for Ligolo reverse tunneling         | [ligolo](https://github.com/sysdream/ligolo-ng) |
| plink.exe       | PuTTY Link: a command-line connection tool similar to SSH | [plink](https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe) |
| socat           | A relay for bidirectional data transfer between two independent data channels | [socat](http://www.dest-unreach.org/socat/) |
| socat.zip       | A relay for bidirectional data transfer between two independent data channels | [socat](http://www.dest-unreach.org/socat/) |

### Post-Exploitation

| Name                 | Description                                              | GitHub Link                         |
|----------------------|----------------------------------------------------------|-------------------------------------|
| DecryptAutoLogon.exe | Tool used to decrypt saved credentials for auto logon    | [DecryptAutoLogon](https://github.com/HarmJ0y/ASREPRoast) |
| Invoke-Mimikatz.ps1  | A PowerShell script to run the famous Mimikatz tool for credential dumping | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| PowerUp.ps1          | A PowerShell script for privilege escalation on Windows machines | [PowerUp](https://github.com/HarmJ0y/PowerUp) |
| PrivescCheck.ps1     | A PowerShell script to enumerate possible paths to escalate privileges on a Windows machine | [PrivescCheck](https://github.com/itm4n/PrivescCheck) |
| Rubeus.exe           | A tool for Kerberos abuse, including ticket requests and renewals | [Rubeus](https://github.com/GhostPack/Rubeus) |
| RunasCs.exe          | A tool for executing commands with different user privileges | [RunasCs](https://github.com/ropnop/kerbrute) |
| RunasCs.zip          | A tool for executing commands with different user privileges | [RunasCs](https://github.com/ropnop/kerbrute) |
| RunasCs_net2.exe     | Another variant of RunasCs for specific .NET environments | [RunasCs](https://github.com/ropnop/kerbrute) |
| Seatbelt.exe         | A C# project that performs a number of security-related checks on a Windows system | [Seatbelt](https://github.com/GhostPack/Seatbelt) |
| SharpHound.exe       | A tool for gathering Active Directory information for BloodHound | [SharpHound](https://github.com/BloodHoundAD/SharpHound3) |
| SharpHound.ps1       | A PowerShell script for gathering Active Directory information for BloodHound | [SharpHound](https://github.com/BloodHoundAD/SharpHound3) |
| mimikatz.exe         | A tool for dumping credentials from Windows systems      | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| mimikatz64.exe       | The 64-bit version of Mimikatz                           | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| mimikatz_trunk       | The development branch of Mimikatz with the latest features | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| mimikatz_trunk.zip   | The development branch of Mimikatz with the latest features | [Mimikatz](https://github.com/gentilkiwi/mimikatz) |
| pypykatz             | A Python implementation of Mimikatz to extract credentials from memory dumps | [pypykatz](https://github.com/skelsec/pypykatz) |
| unix-privesc-check   | A script to check for common misconfigurations and vulnerabilities for Unix privilege escalation | [unix-privesc-check](https://github.com/pentestmonkey/unix-privesc-check) |

### Reverse Shells

| Name                 | Description                                              | GitHub Link                           |
|----------------------|----------------------------------------------------------|---------------------------------------|
| PowerShellGenerators | A collection of PowerShell scripts for various offensive tasks | [PowerShellGenerators](https://github.com/samratashok/nishang) |
| nc                   | Netcat, a versatile networking tool                       | [nc](https://github.com/diegocr/netcat) |
| nc.exe               | The Windows version of Netcat                            | [nc](https://github.com/diegocr/netcat) |
| nc64.exe             | The 64-bit version of Netcat for Windows                 | [nc](https://github.com/diegocr/netcat) |
| pentestmonkey        | A collection of pentesting scripts                        | [pentestmonkey](https://github.com/pentestmonkey/scripts) |
| powercat.ps1         | A PowerShell TCP/IP Swiss army knife, a tool for network interactions | [powercat](https://github.com/besimorhino/powercat) |

### Token Exploitation

| Name                 | Description                                              | GitHub Link                             |
|----------------------|----------------------------------------------------------|-----------------------------------------|
| GodPotato-NET4.exe   | A privilege escalation tool exploiting COM services      | [GodPotato](https://github.com/BeichenDream/GodPotato) |
| JuicyPotato.exe      | A privilege escalation tool for Windows exploiting the token duplication vulnerability | [JuicyPotato](https://github.com/ohpe/juicy-potato) |
| JuicyPotatoNG.exe    | An updated version of JuicyPotato for Windows privilege escalation | [JuicyPotatoNG](https://github.com/antonioCoco/JuicyPotatoNG) |
| JuicyPotatoNG.zip    | An updated version of JuicyPotato for Windows privilege escalation | [JuicyPotatoNG](https://github.com/antonioCoco/JuicyPotatoNG) |
| PrintSpoofer64.exe   | A tool for privilege escalation using the Print Spooler service | [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) |
| SharpEfsPotato.exe   | A tool for exploiting Windows EFS to gain privileges     | [SharpEfsPotato](https://github.com/CCob/SweetPotato) |
| SweetPotato.exe      | Another privilege escalation tool similar to JuicyPotato | [SweetPotato](https://github.com/CCob/SweetPotato) |

### Tools

| Name           | Description                                      | GitHub Link                             |
|----------------|--------------------------------------------------|-----------------------------------------|
| CrackMapExec   | A Swiss army knife for pentesting Windows/Active Directory environments | [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) |
| evil-winrm     | The ultimate WinRM shell for hacking/pentesting  | [evil-winrm](https://github.com/Hackplayers/evil-winrm) |
| impacket       | A collection of Python classes for working with network protocols | [impacket](https://github.com/SecureAuthCorp/impacket) |
| joomscan       | A vulnerability scanner for Joomla CMS           | [joomscan](https://github.com/OWASP/joomscan) |
| kerbrute_linux_amd64 | A tool to quickly brute force and enumerate valid Active Directory accounts | [kerbrute](https://github.com/ropnop/kerbrute) |
| kr             | A tool to quickly brute force and enumerate valid Active Directory accounts | [kerbrute](https://github.com/ropnop/kerbrute) |
| powerview.ps1  | A PowerShell tool to gain network situational awareness on Windows domains | [PowerView](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1) |

## Usage

To use any of these tools, simply navigate to the appropriate directory and execute the binary or script. Ensure that you have the necessary permissions and environment set up for each tool to function correctly.

## Acknowledgements

This configuration was inspired by various tools and configurations available online. Special thanks to the offensive security community for their contributions and shared knowledge.

---

Feel free to contribute to this repository by opening issues or submitting pull requests with improvements and suggestions.
