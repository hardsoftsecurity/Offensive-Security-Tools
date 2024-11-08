import argparse
import subprocess
import sys

def run_command(args, command):
    """
    Run a command and handle errors.
    """
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if args.verbose:
            print(f"Running command: {' '.join(command)}")

        if result.returncode != 0:
            print(f"Error: {result.stderr.strip()}")
            return None
        return result.stdout.strip()
    except Exception as e:
        print(f"Exception: {e}")
        return None

def enumerate_shares(args):
    """
    Enumerate shares using the best available method based on provided arguments.
    """
    if args.user and args.password:
        # Use smbclient with authentication details if provided
        shares_command = [
            "smbclient", "-L", f"//{args.host}", "-U", f"{args.domain}\\{args.user}%{args.password}"
        ]
    elif args.user is None and args.password is None:
        # Try anonymous access with smbclient if no credentials are provided
        shares_command = ["smbclient", "-L", f"//{args.host}"]
    else:
        # Fallback: use nxc for SMB enumeration
        shares_command = ["nxc", "smb", args.host, "--shares"]
        if args.user == "guest" and args.password == "":
            shares_command = ["nxc", "smb", args.host, "-u", "guest", "-p", "", "--shares"]

    output = run_command(args, shares_command)
    if not output:
        print("Failed to enumerate shares.")
        sys.exit(1)

    shares = []
    for line in output.splitlines():
        if "Disk" in line or line.startswith("  "):
            share_name = line.split()[0]
            shares.append(share_name)
    return shares

def list_files_in_share(args, share):
    """
    Recursively list all files in a given share using smbclient.
    """
    print(f"\nListing files for share: {share}")
    command = [
        "smbclient", f"//{args.host}/{share}", "-c", "recurse; ls"
    ]
    if args.user and args.password:
        command += ["-U", f"{args.domain}\\{args.user}%{args.password}"]
    output = run_command(args, command)
    if output is None:
        print(f"Failed to list files in share: {share}")
        return
    
    if args.output:
        with open(args.output, 'a') as f:
            f.write(f"\nShare: {share}\n")
            f.write(output + "\n")
    else:
        print(output)

def main():
    parser = argparse.ArgumentParser(
        description="Enumerate SMB shares and recursively list files.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-H", "--host", required=True, help="IP address of the SMB server")
    parser.add_argument("-d", "--domain", help="Domain name (optional)")
    parser.add_argument("-u", "--user", help="Username (optional)")
    parser.add_argument("-p", "--password", help="Password (optional)")
    parser.add_argument("-o", "--output", help="Output file to save results")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    # Add examples to the help message
    parser.epilog = """
Examples:
  1. Without Authentication (anonymous access):
     python3 smbEnumerationShares.py -H 192.168.1.10

  2. With Guest Access:
     python3 smbEnumerationShares.py -H 192.168.1.10 -u guest -p ''

  3. With Domain, User, and Password:
     python3 smbEnumerationShares.py -H 192.168.1.10 -d MYDOMAIN -u myuser -p mypassword

  4. Save Output to File:
     python3 smbEnumerationShares.py -H 192.168.1.10 -o output.txt

  5. Verbose Mode:
     python3 smbEnumerationShares.py -H 192.168.1.10 -v
    """

    args = parser.parse_args()

    print("Enumerating shares on the server...")
    shares = enumerate_shares(args)
    if not shares:
        print("No shares found.")
        sys.exit(1)

    for share in shares:
        list_files_in_share(args, share)
    print("\nEnumeration completed.")

if __name__ == "__main__":
    main()
