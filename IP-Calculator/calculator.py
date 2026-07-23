def subnet_mask_convert_32bit(Prefix_length):
    # Convert a prefix length to a 32-bit subnet mask.
    prefix_length = int(Prefix_length)
    subnet_mask = ""
    for i in range(32):
        if i < prefix_length:
            subnet_mask += "1"
        else:
            subnet_mask += "0"

    return int(subnet_mask, 2)

    
def ip_to_binary(ip_address):
    # Convert an IP address to its binary representation.
    octets = ip_address.split('.')
    binary_ip = "".join(format(int(octet), '08b') for octet in octets)
    return binary_ip


