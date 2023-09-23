##########README############

Algorithms for BigData Assignment 2
Submitted by Bhawna Bhoria
Roll Number : M22MA003

**********************************************************************************************************

Title : Implementation of Bloom Filter.

1. Use setup.py file to install nltk punkt and stopwords libraries.

2. Set the paths of the Keywords and Filters directory in below files:-
   a. bloom_filter_creation.py
   b. keywords_extraction.py
   c. evaluation.py
   d. lookup.py

3. To run python files, use command "python3 <filename.py>"

Two Methods have been followed:-
First and original method - Uses hashing function from scratch and nltk library stopwords.
Second method uses inbuilt hashing functions and user defined stopwords.

Results:-
It is observed that the first method gives better and reliable results because of two reasons :-
1. nltk library has covered all punctuations and stopwords so only required keywords are extracted which reduces the number of keywords to be hashed for a single file.
2. 64 bit hash function implemented from scratch always gives reliable results whereas inbuilt hash function gives different results in multiple runs, which increases false-positive rate.
Therefore, the false_positive rate in case of second method is high in comparison to original method.