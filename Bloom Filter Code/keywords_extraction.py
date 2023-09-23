import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Firstly use setup.py file to install nltk
# Setting up NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Change the path to input text files accordingly.
input_folder = '/Users/bhawnabhoria/Documents/BigData/Assignment2/Files'

# Change the path to Keywords Directory accordingly.
# Create the "Keywords" folder if it doesn't exist
output_folder = '/Users/bhawnabhoria/Documents/BigData/Assignment2/Keywords'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def extract_keywords(file_path):
    with open(file_path, 'r',   encoding='latin-1') as file:
        text = file.read()
        words = word_tokenize(text.lower())
        # Remove punctuation and stopwords using nltk method.
        words = [word.strip(string.punctuation) for word in words if word not in stopwords.words('english')]
        keywords = list(set(filter(None, words)))
        return keywords


for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    if os.path.isfile(file_path):
        keywords = extract_keywords(file_path)
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
        with open(output_file_path, 'w') as output_file:
            output_file.write(','.join(keywords))
