import requests
from bs4 import BeautifulSoup
import re

# Function to extract text from Wikipedia section
def extract_section_text(url, section_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('span', {'id': section_name}).parent.find_next_sibling('p').get_text()
    return content

# Function to clean and count words
def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    for word in words:
        # Remove brackets and their contents
        word = re.sub(r'\[.*?\]', '', word)
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Test_automation"

# Section name
section_name = "Test-driven_development"

# Extract text from section
section_text = extract_section_text(url, section_name)

# Count words
word_count = count_words(section_text)

# Print word occurrences
for word, count in word_count.items():
    print(f"{word}: {count}")














