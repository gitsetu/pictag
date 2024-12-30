import subprocess


# Find Mac Addresses Function
def find_mac_addresses(target_macs, ip_range="192.168.8.0/24"):
    result = subprocess.check_output(f"sudo nmap -sS {ip_range} | grep MAC", shell=True)
    found_macs=[]
    for mac in target_macs: 
         if mac.lower() in str(result).lower():
             found_macs.append(mac)
    return found_macs


# Test code
if __name__ == "__main__":
    # Example list of target MAC addresses to search for on the network
    # Replace with actual MAC addresses you expect to find
    target_macs = [
        "28:FF:3C:8F:93:B1",  # ATV
        "7C:61:93:84:15:ED"   # htc
    ]

    print("Scanning network...")
    # Call the function to find the specified MAC addresses
    found_devices = find_mac_addresses(target_macs)

    # Display the result
    if found_devices:
        print(f"Found devices:{found_devices}")
    else:
        print("No target MAC addresses found on the network.")