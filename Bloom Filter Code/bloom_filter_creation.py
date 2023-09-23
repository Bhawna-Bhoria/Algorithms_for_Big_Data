import os
import string
import hashing
import shutil

# Change the path to Keywords Directory accordingly.
keywords_dir = '/Users/bhawnabhoria/Documents/BigData/Assignment2/Keywords'


# Change the path to Filters Directory accordingly.
# Create the "Filters" folder if it doesn't exist
filters_dir = '/Users/bhawnabhoria/Documents/BigData/Assignment2/Filters'
if os.path.exists(filters_dir):
    shutil.rmtree(filters_dir)
os.makedirs(filters_dir)

# Define a helper function to construct a Bloom filter
def bloom_filter_create(keywords):
    bloom_filter = [0] * 64
    
    for keyword in keywords:
        # Generate a hash value for the keyword
        hash_value = hashing.hash_function_2(keyword) % 64
        
        # Set the corresponding bit in the Bloom filter to 1
        bloom_filter[hash_value] = 1
    
    return ''.join(str(bit) for bit in bloom_filter)


for filename in os.listdir(keywords_dir):
    single_keywords_file = os.path.join(keywords_dir, filename)
    
    if os.path.isfile(single_keywords_file):
        with open(single_keywords_file, 'r') as keywords_file:
            keywords = keywords_file.read().split(',')
            bloom_filter = bloom_filter_create(keywords)
            
            output_file_path = os.path.join(filters_dir, f"{os.path.splitext(filename)[0]}.txt")
            
            with open(output_file_path, 'w') as output_file:
                output_file.write(bloom_filter)
