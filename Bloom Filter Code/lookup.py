import sys
import os
import hashing

hash_bits = 64
# Change the path to Filters Directory accordingly.
filters_dir = '/Users/bhawnabhoria/Documents/BigData/Assignment2/Filters'  # Replace with the actual path to the "Filters" folder

#In case hashing.py file is not accessible, use this function directly.
def calculate_hash_2(keyword_input):
    hash_code = sum(ord(char) * (indx + 1) for indx, char in enumerate(keyword_input)) % hash_bits
    return hash_code

def do_lookup(keyword):
    hashed_array_result = []
    
    for filename in os.listdir(filters_dir):
        single_filter_file = os.path.join(filters_dir, filename)
        
        if os.path.isfile(single_filter_file):
            with open(single_filter_file, 'r') as filter_file:
                bloom_filter = filter_file.read()
                #Using hash function calculate_hash_2 from hashing.py file
                found = bloom_filter[hashing.calculate_hash_2(keyword) % 64] == '1'
                hashed_array_result.append(found)
    
    return hashed_array_result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use command: python lookup.py <keyword>")
        sys.exit(1)
    
    keyword = sys.argv[1]
    hashed_array_result = do_lookup(keyword)
    
    print(''.join('1' if found else '0' for found in hashed_array_result))


#Results

# python3 lookup.py research
# 111111101110111111111011101111111