from calculator import ip_to_binary, subnet_mask_convert_32bit


def prefix_length_to_subnet_mask(prefix_length):
    # Convert a prefix length to a subnet mask.
    subnet_mask_binary_bits = subnet_mask_convert_32bit(prefix_length)
    subnet_mask_decimal = []
    for i in range(4):
        octet = (subnet_mask_binary_bits >> (24 - 8 * i)) & 0xFF
        subnet_mask_decimal.append(str(octet))
    return '.'.join(subnet_mask_decimal)


def network_address(ip_address, prefix_length):
    # Calculate the network address given an IP address and prefix length.
    subnet_mask = subnet_mask_convert_32bit(prefix_length)
    ip_binary = ip_to_binary(ip_address)

    # Calculate the network address by performing a bitwise AND operation between the IP address and the subnet mask.
    network_address = int(ip_binary, 2) & subnet_mask
    network_address_binary = format(network_address, '032b')
    network_address_decimal = []
    for i in range(4):
        octet = int(network_address_binary[i * 8:(i + 1) * 8], 2)
        network_address_decimal.append(str(octet))
    return '.'.join(network_address_decimal)


def broadcast_address(ip_address, prefix_length):
     # Calculate the network address given an IP address and prefix length.
        subnet_mask = subnet_mask_convert_32bit(prefix_length)
        ip_binary = ip_to_binary(ip_address)

        network_address = int(ip_binary, 2) & subnet_mask
        network_address_binary = format(network_address, '032b')

        # Calculate the broadcast address by performing a bitwise OR operation between the network address and the inverted subnet mask.
        inverted_subnet_mask = ~subnet_mask & 0xFFFFFFFF
        broadcast_address = network_address | inverted_subnet_mask
        broadcast_address_binary = format(broadcast_address, '032b')
        broadcast_address_decimal = []
        for i in range(4):
            octet = int(broadcast_address_binary[i * 8:(i + 1) * 8], 2)
            broadcast_address_decimal.append(str(octet))
        return '.'.join(broadcast_address_decimal)  

def first_host(ip_address, prefix_length):
    # Calculate the first host address given an IP address and prefix length.
    if prefix_length == 32:
        return ip_address  # For /32, the only host is the IP itself.
    if prefix_length == 31:
        return network_address(ip_address, prefix_length)  # For /31, the first host is the network address itself.

    
    network_addr = network_address(ip_address, prefix_length)
    network_addr_binary = ip_to_binary(network_addr)
    first_host_binary = int(network_addr_binary, 2) + 1
    first_host_binary_str = format(first_host_binary, '032b')
    first_host_decimal = []
    for i in range(4):
        octet = int(first_host_binary_str[i * 8:(i + 1) * 8], 2)
        first_host_decimal.append(str(octet))
    return '.'.join(first_host_decimal)


   
   
def last_host(ip_address, prefix_length):
    # Calculate the last host address given an IP address and prefix length.
    if prefix_length == 32:
        return ip_address  # For /32, the only host is the IP itself.
    network_addr = network_address(ip_address, prefix_length)
    network_addr_binary = ip_to_binary(network_addr)    
    if prefix_length == 31:
        return broadcast_address(ip_address, prefix_length)  # For /31, the last host is the broadcast address itself.
    else: 
        broadcast_addr = broadcast_address(ip_address, prefix_length)
        broadcast_addr_binary = ip_to_binary(broadcast_addr)
        last_host_binary = int(broadcast_addr_binary, 2) - 1
        last_host_binary_str = format(last_host_binary, '032b')
        last_host_decimal = []
        for i in range(4):
            octet = int(last_host_binary_str[i * 8:(i + 1) * 8], 2)
            last_host_decimal.append(str(octet))
        return '.'.join(last_host_decimal)

    
def total_hosts(prefix_length):
    # Calculate the total number of hosts given a prefix length.
    prefix_length = int(prefix_length)
    if prefix_length == 32:
        return 1
    elif prefix_length == 31:
        return 2
    else:
        return (2 ** (32 - prefix_length)) - 2

def wildcard_mask(prefix_length):
    # Calculate the wildcard mask given a prefix length.
    subnet_mask = subnet_mask_convert_32bit(prefix_length)
    wildcard_mask = ~subnet_mask & 0xFFFFFFFF
    wildcard_mask_decimal = []
    for i in range(4):
        octet = (wildcard_mask >> (24 - 8 * i)) & 0xFF
        wildcard_mask_decimal.append(str(octet))
    return '.'.join(wildcard_mask_decimal)

def ip_class(ip_address):
    # Determine the class of an IP address.
    first_octet = int(ip_address.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D'
    elif 240 <= first_octet <= 255:
        return 'E'
    else:
        return 'Invalid'

def is_private_ip(ip_address):
    # Determine if an IP address is private or public.
    first_octet = int(ip_address.split('.')[0])
    second_octet = int(ip_address.split('.')[1])
    if (first_octet == 10) or (first_octet == 172 and 16 <= second_octet <= 31) or (first_octet == 192 and second_octet == 168):
        return 'Private'
    else:
        return 'Public'     
