import sys
import hashlib

def calculate_hashes(input_string):
    hashes = []
    hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512, hashlib.blake2b]
    
    for hash_func in hash_functions:
        hash_object = hash_func()
        hash_object.update(input_string.encode('utf-8'))
        hash_value = int.from_bytes(hash_object.digest(), 'big') % (2**64)
        hashes.append(hash_value)
    
    return hashes

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hashing.py <input_string>")
        sys.exit(1)
    
    input_string = sys.argv[1]
    hashes = calculate_hashes(input_string)
    
    print(','.join(str(hash_value) for hash_value in hashes))
