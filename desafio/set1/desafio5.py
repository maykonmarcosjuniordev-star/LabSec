"""
Implement repeating-key XOR

Here is the opening stanza of an important work of the English language:
    Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key;
the first byte of plaintext will be XOR'd against I, the next C, the next E,
then I again for the 4th byte, and so on.

It should come out to:
    0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
    a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

Encrypt a bunch of stuff using your repeating-key XOR function.
Encrypt your mail.
Encrypt your password file.
Your .sig file. Get a feel for it.
I promise, we aren't wasting your time with this.
"""

from desafio3 import find_best_key

def repeating_key_xor(plaintext: str, key: str) -> str:
    """
    Encrypts the plaintext using repeating-key XOR with the given key.
    
    Args:
        plaintext (str): The input plaintext to encrypt.
        key (str): The key to use for encryption.
        
    Returns:
        str: The resulting hex string after encryption.
    """
    # Convert plaintext and key to bytes
    plaintext_bytes = plaintext.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    # Create a bytearray for the result
    result = bytearray()

    key_full = 0
    for i in key_bytes:
        key_full ^= i
    
    # Encrypt using repeating-key XOR
    for i in range(len(plaintext_bytes)):
        byte = plaintext_bytes[i] ^ key_full
        # for j in key_bytes:
        #     byte ^= j
        result.append(byte)
    
    # Convert the result to a hex string and return it
    return result.hex()

if __name__ == "__main__":
    # Example usage
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    
    encrypted_text = repeating_key_xor(plaintext, key)
    print(f"Encrypted text: {encrypted_text}")
    
    # Find the best key for the encrypted text
    best_key, text, score = find_best_key(encrypted_text)
    print(f"Best key: {best_key}, Score: {score}, Decrypted text:\n{text}")