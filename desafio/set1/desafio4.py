"""
Detect single-character XOR

One of the 60-character strings in this file (4.txt) has been encrypted by single-character XOR.

Find it. 
"""

FILE_PATH = 'desafio/inputs/4.txt'

from desafio3 import find_best_key, score_text

def detect_single_char_xor(file_path: str) -> tuple:
    """
    Detect the single-character XOR encrypted string from a file.
    
    Args:
        file_path (str): The path to the file containing hex-encoded strings.
        
    Returns:
        tuple: The best key and the decoded string.
    """
    best_key = -1
    best_line = ''
    best_score = float('-inf')
    
    with open(file_path, 'r') as file:
        for line in file:
            hex_string = line.strip()
            key, line, score = find_best_key(hex_string)
            if score > best_score:
                best_score = score
                best_key = key
                best_line = line
                # print(f"New best key: '{chr(best_key)}' with score: {best_score}\nLine: {best_line}\n")
            
    
    return best_key, best_line
    

if __name__ == "__main__":
    key, decoded_string = detect_single_char_xor(FILE_PATH)
    assert key != -1, "No valid key found."
    assert decoded_string, "No valid decoded string found."
    print(f"Best Key: {key}")
    print(f"Score: {score_text(decoded_string)}")
    print(f"Decoded String: {decoded_string}", end='')