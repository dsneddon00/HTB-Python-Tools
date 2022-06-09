import requests
import re
from bs4 import BeautifulSoup

PAGE_URL = "http://" + str(input("Input host IP and port ( <HOST>:<IP> ) -> "))

resp = requests.get(PAGE_URL)


def getHtmlOf(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'HTTP status code of {response.status_code} returned, but 200 was expected. Exiting...')
        exit(1)
    else:
        return response.content.decode()

dump = getHtmlOf(PAGE_URL)
beautify = BeautifulSoup(dump, "html.parser")
raw = beautify.get_text()
total = re.findall(r'\w+', raw)

wordCount = {}

for word in total:
    if(word not in wordCount):
        wordCount[word] = 1
    else:
        cur = wordCount.get(word)
        wordCount[word] = cur + 1

topWords = sorted(wordCount.items(), key=lambda item: item[1], reverse=True)

for i in range(10):
    print(topWords[i][0])
