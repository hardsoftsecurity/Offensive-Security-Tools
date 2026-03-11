# Offensive Security Tools Collection

This repository is a curated collection of binaries, scripts, and frameworks used during OSCP preparation and various CTF challenges. It is organized by attack phase to allow for quick access during engagements.

> [!IMPORTANT]
> **Submodules have been removed.** All tools are now hosted directly within this repository for easier portability.

## 🚀 Quick Start

Clone the repository:
```bash
git clone https://github.com/hardsoftsecurity/Offensive-Security-Tools.git
cd Offensive-Security-Tools
```

## Tools List

### 🏗️ Active Directory (AD)

| Tool | Description |
| :--- | :--- |
| **BadSuccessor.ps1** | PowerShell script for AD exploitation/enumeration |
| **Certipy.exe** | Tool for enumerating and exploiting Active Directory Certificate Services (AD CS) |
| **DFSCoerce** | Tool to coerce authentication via DFSRP |
| **gMSADumper.py** | Extracts passwords from Group Managed Service Accounts (gMSA) |
| **kerbrute** | Rapid Active Directory enumeration and brute force via Kerberos Pre-Authentication |
| **krbrelayx** | Toolkit for Kerberos relay attacks (includes addspn, dnstool, and printerbug) |
| **ntlm_theft** | Generates multiple types of NTLMv2 hash theft files (xlsx, docx, lnk, etc.) |
| **PetitPotam** | Tool to coerce Windows hosts to authenticate to other machines via MS-EFSRPC |
| **PKINITtools** | Utilities for PKINIT and certificate-based auth (gettgtpkinit, gets4uticket) |
| **Powermad** | PowerShell tools for AD MachineAccountQuota exploitation and DNS updates |
| **PowerView.ps1** | Situational awareness tool for Windows domains |
| **pyLAPS** | Python tool to retrieve LAPS passwords from AD |
| **pywhisker** | Python tool for Shadow Credentials exploitation |
| **Rubeus.exe** | Toolset for raw Kerberos interaction and abuses |
| **SharpDPAPI.exe** | C# port of Mimikatz DPAPI functionality for credential/backup key extraction |
| **SharpHound** | BloodHound ingestors (C# and PowerShell versions) |
| **SpoolSample.exe** | Tool to coerce Windows hosts to authenticate via the Print Spooler service |
| **targetedKerberoast**| Python script for targeted Kerberoasting attacks |
| **username_generator**| Script to generate potential AD usernames based on naming conventions |
| **winrmexec** | WinRM shell execution and lateral movement tool |

---

### 📜 Custom Scripts

Personal automation scripts designed for rapid enumeration, discovery, and environment checks.

| Tool | Description |
| :--- | :--- |
| **checkDisabledFunc.php** | PHP script to identify disabled functions in restricted web environments |
| **InitialScanOSCP.py** | Automation script for initial target reconnaissance |
| **pingHostDiscovery.py** | Python-based ICMP scanner for identifying live hosts on a network |
| **portscan.sh** | Lightweight bash script for quick port discovery |
| **smbEnumerationShares.py** | Script to automate the discovery and listing of SMB shares |
| **uncommonWinPorts.ps1** | PowerShell script to identify non-standard open ports on Windows targets |

---

### 🔍 Enumeration & Scouting

This section covers tools for web path discovery, system configuration auditing, and network scanning.

| Tool | Description |
| :--- | :--- |
| **dirsearch** | Advanced web path brute-forcing tool with custom wordlists and threading |
| **Get-ServiceAcl.ps1**| PowerShell script to enumerate ACLs of Windows services |
| **gobuster** | Tool used to discover URIs, DNS subdomains, and virtual host names |
| **linpeas.sh** | Privilege escalation path finder for Linux/Unix systems |
| **nmap** | Industry-standard network scanner (Linux & Windows binaries included) |
| **pspy64** | Monitor Linux processes in real-time without root permissions |
| **SetAcl** | Advanced tool for managing Windows permissions (x64 and x86 versions) |
| **Sysinternals** | Full suite of Microsoft troubleshooting and security utilities (AccessChk, PsExec, etc.) |
| **winPEAS** | Windows Privilege Escalation Awesome Scripts (Batch and .exe versions) |

---

### 🏃 Lateral Movement & GPO Abuse

Tools focused on pivoting through the domain, exploiting Group Policy Objects, and switching user contexts.

| Tool | Description |
| :--- | :--- |
| **GPOwned** | Python tool to identify and exploit insecure GPOs by searching for sensitive information |
| **Group3r.exe** | Tool for finding vulnerabilities in AD Group Policy from a user's perspective |
| **RunasCs.exe** | A better `runas` for Windows, allowing command execution with different credentials including networking |
| **SharpGPOAbuse.exe**| C# tool to abuse GPO permissions (e.g., adding a local admin or a startup script) |
| **SharpGPO.exe** | Utility to enumerate and interact with Group Policies |
| **Whisker.exe** | C# tool for Shadow Credentials exploitation to take over accounts |

---

### 📦 Miscellaneous Utilities

A collection of wordlists, debugging scripts, and specialized data-dumping tools.

| Tool | Description |
| :--- | :--- |
| **directoryLists** | Targeted wordlists for API endpoints, SNMP, and web directory fuzzing (IIS, Raft, etc.) |
| **gdb_commands** | Python scripts and `.gdbinit` for binary analysis (pattern generation, checksec) |
| **git-dumper** | A tool to dump a git repository from a website when the `.git` folder is exposed |
| **ntlm_theft** | Generates malicious templates (docx, lnk, etc.) to capture NTLM hashes over the network |
| **passwordList** | High-probability password lists (e.g., Top 1 Million list) |

---

### 🎣 Phishing & Initial Access

Tools for generating malicious documents and weaponized office files to obtain initial foot-holds.

| Tool | Description |
| :--- | :--- |
| **badodf** | Python tool to create malicious ODT files that trigger NTLM credential theft or execute commands |
| **macro_reverse_shell** | Automation script to generate weaponized Office macros for reverse shell connectivity |

---

### 🧱 Pivoting & Tunneling

Essential tools for bypassing firewalls, creating network tunnels, and routing traffic through compromised hosts.

| Tool | Description |
| :--- | :--- |
| **chisel** | Fast TCP/UDP tunnel over HTTP, secured via SSH. Includes Linux and Windows (x64/x86) binaries |
| **ligolo-ng** | Advanced tunneling tool that uses a TUN interface to simulate a real network connection (Agent & Proxy) |
| **plink.exe** | PuTTY command-line connection utility, used for SSH remote port forwarding on Windows |
| **socat** | Multipurpose relay tool (the "Netcat on steroids") for port forwarding and complex networking |

---

### 🐍 Post-Exploitation & Credential Dumping

Tools for extracting secrets, escalating privileges, and auditing system security after an initial compromise.

| Tool | Description |
| :--- | :--- |
| **DecryptAutoLogon.exe** | Recovers cleartext credentials from Windows AutoLogon registry keys |
| **mimikatz** | The industry-standard tool for credential dumping (includes trunk versions for x86/x64 and PowerShell) |
| **pamLogger / pamspy** | Linux-based tools to intercept and log credentials via the PAM (Pluggable Authentication Modules) |
| **PowerUp / PrivescCheck** | PowerShell scripts for finding common Windows misconfigurations and PrivEsc vectors |
| **RemotePotato0** | Tool to achieve local privilege escalation from a domain user to SYSTEM via NTLM relay |
| **RunasCs** | Advanced `runas` replacement (includes .NET 2.0 version for legacy compatibility) |
| **Seatbelt.exe** | C# project for performing local system "safety checks" for privilege escalation |
| **SharpHound** | BloodHound collectors (Current v2.5+ and Legacy versions included for varying .NET environments) |
| **unix-privesc-check** | Shell script to find common privilege escalation vectors on Unix/Linux systems |

---

### 🐚 Reverse Shells & Web Shells

A versatile collection of payloads for establishing command execution across various web technologies and operating systems.

| Tool | Description |
| :--- | :--- |
| **demontime** | Obfuscated PowerShell reverse shell templates designed to bypass basic AV signatures |
| **forward-shell** | Python-based "Forward Shell" for environments where reverse/bind shells are impossible (uses command execution via web requests) |
| **JWT_Forward_Shell** | Specialized forward shell that utilizes JSON Web Tokens for command transport |
| **nc / Netcat** | The "TCP/IP Swiss Army Knife" (includes Linux and Windows x86/x64 binaries) |
| **pentestmonkey** | The classic, reliable PHP reverse shell and various one-liners |
| **powercat.ps1** | A PowerShell-native implementation of Netcat |
| **PowerShellGenerators**| Automation scripts to generate custom, encoded PowerShell reverse shell strings |
| **Web Shells** | Multi-platform web shells including `.aspx` (IIS), `.jsp` (Tomcat/Java), and `.js` (Node.js) |
| **mssql_shell.py** | Specialized script for obtaining a shell via MSSQL `xp_cmdshell` exploitation |

---

### 🥔 Token Exploitation & Potato Attacks

Specialized tools for local privilege escalation (LPE) via service account token impersonation.

| Tool | Description |
| :--- | :--- |
| **FullPowers.exe** | Recovers "hidden" default privileges in a service trace (e.g., getting SeImpersonate back) |
| **GodPotato-NET4.exe** | Modern impersonation exploit targeting .NET 4 environments; effective on newer Windows builds |
| **JuicyPotato / NG** | The classic BITS service exploit (NG version is optimized for newer OS versions) |
| **PrintSpoofer64.exe** | Abuse of the Print Spooler service for SYSTEM escalation (extremely reliable on Server 2016/2019) |
| **SharpEfsPotato.exe** | C# implementation of the EFS-based impersonation exploit |
| **SweetPotato.exe** | A collection of various Potato-style exploits (Juicy, PrintSpoofer, etc.) in a single binary |

---

### 🧰 General Frameworks & Power Tools

Foundational tools for protocol interaction, password manipulation, and specialized service scanning.

| Tool | Description |
| :--- | :--- |
| **clipBoardMonitor.ps1**| Stealthy PowerShell script to monitor and log clipboard contents for credentials |
| **CrackMapExec (CME)** | The ultimate post-exploitation tool for AD; automates credential spraying, dumping, and lateral movement |
| **evil-winrm** | The best shell for WinRM exploitation; supports file uploads, command history, and script loading |
| **impacket** | Full suite of Python classes for working with network protocols (SMB, MSSQL, Kerberos, etc.) |
| **joomscan** | Specialized vulnerability scanner for identifying flaws in Joomla CMS installations |
| **KeeThief / KeeTheft** | Tools for extracting KeePass master keys from the memory of a running process |
| **kerbrute** | High-performance Kerberos brute-forcing and enumeration (Linux binary) |
| **maskprocessor** | High-performance word generator based on character masks for advanced password cracking |
| **kwprocessor** | Advanced keyboard-walk generator (e.g., "qwerty") for creating custom dictionaries |

---

## Usage

To use any of these tools, simply navigate to the appropriate directory and execute the binary or script. Ensure that you have the necessary permissions and environment set up for each tool to function correctly.

## Acknowledgements

This configuration was inspired by various tools and configurations available online. Special thanks to the offensive security community for their contributions and shared knowledge.

---

Feel free to contribute to this repository by opening issues or submitting pull requests with improvements and suggestions.
