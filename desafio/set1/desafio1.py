"""
    Convert hex to base64
    
The string:
    49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:
    SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

    So go ahead and make that happen.
    You'll need to use this code for the rest of the exercises.

Cryptopals Rule
    Always operate on raw bytes, never on encoded strings.
    Only use hex and base64 for pretty-printing.
"""

import base64

HEX_STRING = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

B64_STRING = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hex_to_base64_using_libs(hex_string: str) -> str:
    """
    Convert a hex string to a base64 encoded string.
    
    Args:
        hex_string (str): The input hex string.
        
    Returns:
        str: The base64 encoded string.
    """
    # Decode the hex string to bytes
    byte_array = bytes.fromhex(hex_string)
    # Encode the byte array to base64
    base64_bytes = base64.b64encode(byte_array)
    # Convert the base64 bytes to a string
    base64_string = base64_bytes.decode('utf-8')
    return base64_string

def base64_to_hex_lib(base64_string: str) -> str:
    """
    Convert a base64 encoded string to a hex string using libraries.
    
    Args:
        base64_string (str): The input base64 encoded string.
        
    Returns:
        str: The hex string.
    """
    # Decode the base64 string to bytes
    byte_array = base64.b64decode(base64_string)
    # Convert the byte array to a hex string
    hex_string = byte_array.hex()
    return hex_string

def hex_to_base64(hex_string: str) -> str:
    """
    Convert a hex string to a base64 encoded string without using libraries.
    
    Args:
        hex_string (str): The input hex string.
        
    Returns:
        str: The base64 encoded string.
    """
    # ensure the hex string's length is a multiple of 2
    # otherwise, it cannot be converted to bytes correctly
    if len(hex_string) % 2 != 0:
        raise ValueError("Hex string must have an even length")

    # Convert hex to bytes
    byte_array = bytearray.fromhex(hex_string)
    
    # Base64 encoding table
    b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Prepare the base64 result
    b64_result = []
    
    # Process the byte array in chunks of 3 bytes (24 bits)
    for i in range(0, len(byte_array), 3):
        remaing_bytes = byte_array[i:]
        if i + 3 > len(remaing_bytes):
            # padding with zero bytes if the last chunk is less than 3 bytes
            remaing_bytes = byte_array[i:] + b'\x00' * (3 - (len(remaing_bytes) - i))
        # Get the next 3 bytes
        chunk = remaing_bytes[:3]
        # Convert the 3 bytes to 24 bits
        # using byteorder 'big' to ensure the most significant byte is first
        bits = int.from_bytes(chunk, 'big')
        
        # Get the 4 base64 characters from the 24 bits
        for j in range(18, -1, -6):
            # Extract 6 bits at a time
            # shift the bits right by j and mask with 0x3F to get the index
            index = (bits >> j) & 0x3F
            # Append the corresponding base64 character
            b64_result.append(b64_table[index])
    
    # Add padding if necessary
    while len(b64_result) % 4 != 0:
        b64_result.append('=')
    
    return ''.join(b64_result)

if __name__ == "__main__":
    # base64_lib_result = hex_to_base64_using_libs(HEX_STRING)
    base64_result = hex_to_base64(HEX_STRING)
    verify_counter_answer = hex_to_base64_using_libs(HEX_STRING)
    print(base64_result, verify_counter_answer, sep='\n')
    print(base64_result == verify_counter_answer)  # Should print True if the conversion is correct
    print("================")
    hex_lib_result = base64_to_hex_lib(base64_result)
    print(hex_lib_result, HEX_STRING, sep='\n')
    print(hex_lib_result == HEX_STRING)  # Should print True if the conversion is correct