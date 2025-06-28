"""
Single-byte XOR cipher

The hex encoded string:
    1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character.

Find the key, decrypt the message.

Devise some method for "scoring" a piece of English plaintext.
    Character frequency is a good metric.
Evaluate each output and choose the one with the best score.
"""

import string
from collections import Counter

TEXT = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def get_string_from_hex(hex_string: str) -> str:
    """
    Convert a hex string to a regular string.
    
    Args:
        hex_string (str): The input hex string.
        
    Returns:
        str: The decoded string.
    """
    # Convert the hex string to bytes
    byte_array = bytes.fromhex(hex_string)

    # Convert the byte array to a string and return it
    return byte_array.decode('utf-8', errors='ignore')

def single_byte_xor(hex_string: str, key: int) -> str:
    """
    XOR a hex-encoded string with a single byte key.
    
    Args:
        hex_string (str): The input hex string.
        key (int): The single byte key (0-255).
        
    Returns:
        str: The resulting hex string after XOR operation.
    """
    # Convert the hex string to bytes
    byte_array = bytes.fromhex(hex_string)
    
    # Perform XOR operation with the key
    xor_result = bytearray(b ^ key for b in byte_array)
    
    # Convert the result back to a hex string and return it
    return xor_result.hex()

def score_text(text: str) -> int:
    """
    Score a text based on character frequency and common English words.
    
    Args:
        text (str): The input text to score.
        
    Returns:
        int: The score of the text.
    """
    # Define a simple character frequency table for English letters
    english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    # Count the frequency of each character in the text
    char_count = Counter(text.upper())
    
    # Calculate the score based on character frequency
    # adding a weight to each character based on its position in the frequency table
    score = sum(char_count[char]*(27-idx) for idx, char in enumerate(english_freq) if char in char_count)
    
    # Penalize non-printable characters
    score -= sum(1 for c in text if c not in string.printable)
    
    return score

def find_best_key(hex_string: str) -> tuple[int, str, int | float]:
    """
    Find the best single byte key for the given hex string.
    
    Args:
        hex_string (str): The input hex string.
        
    Returns:
        tuple: The best key, the decrypted text, and the score of the decrypted text.
    """
    # initialize variables to track the best score and corresponding key
    # with the lowest possible score
    best_score = float('-inf')
    best_key = -1
    best_text = ""
    
    # test all possible single byte keys (0-255)
    for key in range(256):
        # XOR the hex string with the current key
        decrypted_hex = single_byte_xor(hex_string, key)
        # Convert the decrypted hex back to a string
        decrypted_text = get_string_from_hex(decrypted_hex)
        
        # Score the decrypted text
        score = score_text(decrypted_text)
        
        # If this score is better than the best found so far, update best values
        if score > best_score:
            best_score = score
            best_key = key
            best_text = decrypted_text
            # print(f"New Best:\nKey: {best_key} - Score: {best_score} - Text: {best_text}")

    #best_text = bytes.fromhex(best_text).decode('utf-8', errors='ignore')
    return best_key, best_text, best_score

if __name__ == "__main__":
    best_key, decrypted_text, score = find_best_key(TEXT)
    print(f"Best Key: {best_key} (Character: {chr(best_key)}), Score: {score}")
    
    # Check if the decrypted text is printable
    if all(c in string.printable for c in decrypted_text):
        print(f"Decrypted Text: \n{decrypted_text}")
    else:
        print("The decrypted text contains non-printable characters.")