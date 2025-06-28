"""
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
    1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
    686974207468652062756c6c277320657965

... should produce:
    746865206b696420646f6e277420706c6179
"""

HEX1 = '1c0111001f010100061a024b53535009181c'
HEX2 = '686974207468652062756c6c277320657965'

ANW = '746865206b696420646f6e277420706c6179'

def fixed_xor(hex_string1: str, hex_string2: str) -> str:
    """
    Perform a fixed XOR operation on two hex strings of equal length.
    
    Args:
        hex_string1 (str): The first hex string.
        hex_string2 (str): The second hex string.
        
    Returns:
        str: The resulting hex string after XOR operation.
    """
    if len(hex_string1) != len(hex_string2):
        raise ValueError("Hex strings must be of equal length")
    
    # Convert hex strings to byte arrays
    bytes1 = bytes.fromhex(hex_string1)
    bytes2 = bytes.fromhex(hex_string2)
    
    xor_result = bytearray()

    # Perform XOR operation on each byte
    for i in range(len(bytes1)):
        a = bytes1[i]
        b = bytes2[i]
        if not (0 <= a < 256) or not (0 <= b < 256):
            raise ValueError("Hex strings must represent valid byte values (0-255)")
        # Generate the XOR result

        xor_result.append(a ^ b)

    # Convert the result back to a hex string and return it
    return xor_result.hex()

if __name__ == "__main__":
    result = fixed_xor(HEX1, HEX2)
    print(f"Result:   {result}")
    print(f"Expected: {ANW}")
    print (f"Result matches expected? -> {result == ANW}")
    assert result == ANW, "The XOR result does not match the expected output."