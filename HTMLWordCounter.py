import requests
import re
import click
from bs4 import BeautifulSoup



def getHtmlOf(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'HTTP status code of {response.status_code} returned, but 200 was expected. Exiting...')
        exit(1)
    else:
        return response.content.decode()

def countOccurrencesIn(word_list, min_length):
    word_count = {}

    for word in word_list:
        if(len(word) < min_length):
           continue
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

def getTopWordsFrom(url, min_length):
    all_words = getAllWordsFrom(url)
    occurrences = countOccurrencesIn(all_words, min_length)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True) # lambda helps sorts the dictionary by values

@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of webpage to extract from.')
@click.option('--length', '-l', default=0, help='Minimum word length (default: 0, no limit).')
@click.option('--results', '-r', default=10, help='How many results printed out to the user (default: 10, no limit).')


def main(url, length, results): 
    top_words = getTopWordsFrom(url, length)

    for i in range(results):
        print(top_words[i][0])

if __name__ == '__main__':	
    main()
