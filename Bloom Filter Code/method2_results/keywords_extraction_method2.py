import os
import string
import shutil

# Change the path to input text files accordingly.
input_folder = '/Users/bhawnabhoria/Documents/BigData/Assignment2/Files'  


# Change the path to Keywords Directory accordingly.
# Create the "Keywords" folder if it doesn't exist
output_folder = '/Users/bhawnabhoria/Documents/BigData/Assignment2/Keywords'
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

# Create the output directory after verifying.
os.makedirs(output_folder)
#defining set of stopwords - without nltk.
stopwords = set([
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will',
    'with', 'the', 'not', 'for', 'yet', 'also', 'she', 'them', 'they', 'only', 'there', 'their'
])


def extract_keywords(file_path):
    with open(file_path, 'r',  encoding='latin-1') as file:
        text = file.read()
        words = text.lower().split()
        
        # Remove punctuation and stopwords
        words = [
            word.strip(string.punctuation) for word in words
            if word.strip(string.punctuation) and word not in stopwords
        ]
        
        # Remove duplicates
        keywords = list(set(words))
        
        return keywords



for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    
    if os.path.isfile(file_path):
        keywords = extract_keywords(file_path)
        
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
        
        with open(output_file_path, 'w') as output_file:
            output_file.write(','.join(keywords))
