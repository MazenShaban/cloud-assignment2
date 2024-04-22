# Import "re" for regular expressions.
import re

# Import the set of stop words.
from nltk.corpus import stopwords

# Download the set of stop words.
import nltk
nltk.download('stopwords')

# Read and store the text file
with open("paragraphs.txt", 'r') as file:
    text = file.read()

# Get the words from the text and remove non-alphanumeric characters.
words = re.findall(r'\b\w+\b', text.lower())

# store the set of the stop words
stop_words = set(stopwords.words("english"))

# Remove stop words and store the rest of words.
filtered_words = [word for word in words if word not in stop_words]

# Output the frequency of each word as a dictionary
dictionary = {}
for word in filtered_words:
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1
        
# Print the results
for key, value in dictionary.items():
    print(f"{key}: {value}")
