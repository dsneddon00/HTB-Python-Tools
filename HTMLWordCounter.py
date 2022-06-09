import requests
import re
from bs4 import BeautifulSoup

PAGE_URL = "http://" + str(input("Input host IP and port ( <HOST>:<IP> ) -> "))


def getHtmlOf(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'HTTP status code of {response.status_code} returned, but 200 was expected. Exiting...')
        exit(1)
    else:
        return response.content.decode()

def countOccurrencesIn(word_list):
    word_count = {}

    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            current_count = word_count.get(word)
            word_count[word] = current_count + 1
    return word_count

def getAllWordsFrom(url):
    html = getHtmlOf(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    return re.findall(r'\w+', raw_text)

def getTopWordsFrom(url):
    all_words = getAllWordsFrom(url)
    occurrences = countOccurrencesIn(all_words)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True) # lambda helps sorts the dictionary by values

top_words = getTopWordsFrom(PAGE_URL)

for i in range(20):
    print(top_words[i][0])
