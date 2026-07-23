from validator import is_valid_ip
from ip_utils import broadcast_address, first_host, ip_class, is_private_ip, last_host, network_address, prefix_length_to_subnet_mask, total_hosts, wildcard_mask

IP_ADDRESS=input("Enter the IP address: ").strip()

Prefix_length = input("Enter the prefix length (e.g., 24 for /24): ").strip()


if is_valid_ip(IP_ADDRESS) and Prefix_length.isdigit() and (0 <= int(Prefix_length) <= 32):
    print(f"Valid IP address: {IP_ADDRESS}/{Prefix_length}")
    print(f"Subnet mask: {prefix_length_to_subnet_mask(Prefix_length)}")
    print(f"Network address: {network_address(IP_ADDRESS, int(Prefix_length))}")
    print(f"Broadcast address: {broadcast_address(IP_ADDRESS, int(Prefix_length))}")
    print(f"First host: {first_host(IP_ADDRESS, int(Prefix_length))}")
    print(f"Last host: {last_host(IP_ADDRESS, int(Prefix_length))}")
    print(f"Total hosts: {total_hosts(Prefix_length)}")
    print(f"Wildcard mask: {wildcard_mask(Prefix_length)}")
    print(f"IP Class: {ip_class(IP_ADDRESS)}")
    print(f"Private/Public: {is_private_ip(IP_ADDRESS)}")

else:
    print("Invalid IP address or prefix length.")




"""
IP Address       : 192.168.10.20
Subnet Mask      : 255.255.255.0
Network Address  : 192.168.10.0
Broadcast Address: 192.168.10.255
First Host       : 192.168.10.1
Last Host        : 192.168.10.254
Total Hosts      : 254
Wildcard Mask    : 0.0.0.255
Class            : C
Private/Public   : Private
"""
    