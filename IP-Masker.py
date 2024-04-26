import random

# Function to mask an IP address
def mask_ip(ip_address):
    # Ensure there are at most 5 X's
    num_x = min(5, len([c for c in ip_address if c.isdigit()]))
    # Generate random indices to replace with digits
    indices = random.sample([i for i, c in enumerate(ip_address) if c.isdigit()], num_x)
    masked_ip = list(ip_address)
    for i in indices:
        # Replace the digit at the index with 'X'
        masked_ip[i] = 'X'
    return ''.join(masked_ip)

# Read IP addresses from ips.txt, mask them, and replace ips.txt with masked IPs
with open('ips.txt', 'r+') as file:
    lines = file.readlines()
    file.seek(0)  # Reset file pointer to the beginning
    file.truncate()  # Clear the file content
    for line in lines:
        ip_address = line.strip()
        masked_ip = mask_ip(ip_address)
        file.write(masked_ip + '\n')
