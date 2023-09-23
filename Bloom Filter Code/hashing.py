import sys

# Define the range for the hash codes
hash_bits = 64

# Five universal hash functions
def calculate_hash_1(keyword_input):
    hash_code = sum(ord(char) for char in keyword_input) % hash_bits
    return hash_code

def calculate_hash_2(keyword_input):
    hash_code = sum(ord(char) * (indx + 1) for indx, char in enumerate(keyword_input)) % hash_bits
    return hash_code

def calculate_hash_3(keyword_input):
    hash_code = sum((indx + 1) * (ord(char) - ord('a') + 1) for indx, char in enumerate(keyword_input)) % hash_bits
    return hash_code

def calculate_hash_4(keyword_input):
    hash_code = sum((indx + 1) * (ord(char) - ord('a') + 1) ** 2 for indx, char in enumerate(keyword_input)) % hash_bits
    return hash_code

def calculate_hash_5(keyword_input):
    hash_code = sum((indx + 1) * ord(char) ** 2 for indx, char in enumerate(keyword_input)) % hash_bits
    return hash_code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use command: python hashing.py <keyword_input>")
        sys.exit(1)
    
    keyword_input = sys.argv[1]
    hash_codes = [
        calculate_hash_1(keyword_input),
        calculate_hash_2(keyword_input),
        calculate_hash_3(keyword_input),
        calculate_hash_4(keyword_input),
        calculate_hash_5(keyword_input)
    ]
    
    print(','.join(str(code) for code in hash_codes))

#Results
# python3 hashing.py algorithm
# 7,27,59,19,19