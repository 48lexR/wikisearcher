from bs4 import BeautifulSoup
from requests import get
from numpy.random import choice
import sys
from playsound import playsound

def main():
    # start
    search_item: str = input("Word to search for:\n").lower()
    link = input("Link to start at:\n")
    soup: BeautifulSoup = BeautifulSoup(get(link).text, 'html.parser') # mostly irrelevant data, but this is the entire website's content
    text: str = soup.get_text().lower().strip()
    counter: int = 0
    while(text.find(search_item) == -1):

        try:
            link = "https://en.wikipedia.org/" + choice([x.get('href') for x in soup.find_all('a')])
        except TypeError:
            playsound("fail-buzzer-01.wav")
            sys.stdout.write("Could not read. Input new link:\n")
            link = input()
            sys.stdout.flush()

        soup = BeautifulSoup(get(link).text, 'html.parser')
        text = soup.get_text().lower().strip()
        counter += 1
        sys.stdout.write(str("Trying {}\n".format(link)))
        sys.stdout.flush()
        # print(link)
    else:
        playsound("ding-36029.mp3")
        print("Found {} at {} in {} tries.".format(search_item, link, counter))

if __name__ == "__main__":
    main()