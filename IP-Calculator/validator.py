def is_valid_ip(ip_address):
    # Split the IP address into its octets
    octets = ip_address.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False

    # Check each octet to ensure it's a valid number between 0 and 255
    for i in octets:
        if not i.isdigit() or not (0 <= int(i) <= 255):
            return False

    return True
