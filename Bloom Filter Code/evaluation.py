import sys
import os
import csv
import hashing

# Define the path to the "Filters" folder
filters_folder = '/Users/bhawnabhoria/Documents/BigData/Assignment2/Filters'  # Replace with the actual path to the "Filters" folder

# Define the path to the testing queries file
testing_queries_file = '/Users/bhawnabhoria/Documents/BigData/Assignment2/testing_queries.csv'  # Replace with the actual path to the testing queries file

# Define a helper function to perform the lookup
def perform_lookup(keyword):
    hashed_array_result = []
    
    for filename in os.listdir(filters_folder):
        filter_file_path = os.path.join(filters_folder, filename)
        
        if os.path.isfile(filter_file_path):
            with open(filter_file_path, 'r') as filter_file:
                bloom_filter = filter_file.read()
                
                # Check if the corresponding bit in the Bloom filter is set to 1
                found = bloom_filter[hashing.calculate_hash_2(keyword) % 64] == '1'
                
                hashed_array_result.append(found)
    
    return hashed_array_result

if __name__ == "__main__":
    # Read the testing queries from the file
    queries = []
    with open(testing_queries_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            queries.append(row[0])
    
    # Perform the lookup for each query and calculate false positive rates
    false_positive_rates = []
    total_queries = len(queries)
    
    for i in range(32):
        false_positives = 0
        for query in queries:
            hashed_array_result = perform_lookup(query)
            if hashed_array_result[i]:
                false_positives += 1
        
        false_positive_rate = false_positives / total_queries
        false_positive_rates.append(false_positive_rate)
    output_file = 'false_positive.txt'
    with open(output_file, 'w') as file:
        for rate in false_positive_rates:
            file.write(str(rate) + '\n')
