import subprocess
import ipaddress
import sys

def ping_host(ip, verbose=False):
    """
    Pings a single IP address to check if the host is alive.
    
    Args:
        ip (str): The IP address to ping.
        verbose (bool): If True, print each ping attempt.
        
    Returns:
        bool: True if the host responded to the ping, False otherwise.
    """
    if verbose:
        print(f"Pinging {ip}...")
        
    try:
        output = subprocess.check_output(["ping", "-c", "1", "-W", "1", str(ip)], stderr=subprocess.STDOUT, universal_newlines=True)
        if "1 received" in output:
            if verbose:
                print(f"Host {ip} is alive.")
            return True
    except subprocess.CalledProcessError:
        if verbose:
            print(f"Host {ip} did not respond.")
        return False

    return False

def discover_hosts(network, verbose=False):
    """
    Discovers live hosts within a given network.
    
    Args:
        network (str): The network in CIDR notation (e.g., '192.168.0.0/24').
        verbose (bool): If True, print each step of the discovery process.
        
    Returns:
        list: A list of IP addresses that responded to the ping.
    """
    live_hosts = []
    net = ipaddress.ip_network(network, strict=False)

    if verbose:
        print(f"Scanning network {network}...")

    for ip in net.hosts():
        if ping_host(ip, verbose):
            live_hosts.append(str(ip))

    return live_hosts

if __name__ == "__main__":
    """
    Main function to run the script. The network should be passed as a command-line argument.
    Usage: python discover_hosts.py 192.168.0.0/24 --verbose
    """
    if len(sys.argv) < 2:
        print("Usage: python discover_hosts.py <network> [--verbose]")
        sys.exit(1)

    network = sys.argv[1]
    verbose = "--verbose" in sys.argv

    live_hosts = discover_hosts(network, verbose)

    if live_hosts:
        print(f"\nLive hosts in network {network}:")
        for host in live_hosts:
            print(host)
    else:
        print(f"\nNo live hosts found in network {network}.")
