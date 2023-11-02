import re
from Crypto.Hash import keccak


def is_checksum_address(address):
    address = address.replace('0x', '')
    address_hash = keccak.new(digest_bits=256)
    address_hash = address_hash.update(address.lower().encode('utf-8')).hexdigest()

    for i in range(0, 40):
        # The nth letter should be uppercase if the nth digit of casemap is 1
        if ((int(address_hash[i], 16) > 7 and address[i].upper() != address[i]) or
                (int(address_hash[i], 16) <= 7 and address[i].lower() != address[i])):
            return False
    return True


def is_address(address):
    if not re.match(r'^(0x)?[0-9a-f]{40}$', address, flags=re.IGNORECASE):
        # Check if it has the basic requirements of an address
        return False
    elif re.match(r'^(0x)?[0-9a-f]{40}$', address) or re.match(r'^(0x)?[0-9A-F]{40}$', address):
        # If it's all small caps or all all caps, return true
        return True
    else:
        # Otherwise check each case
        return is_checksum_address(address)
