from bs4 import BeautifulSoup
from requests import *
import numpy.random as rand
import sys

def main():
    # start
    search = "piss"
    link = f"https://www.igi-global.com/dictionary/a-foucauldian-perspective-on-using-the-transparency-framework-in-learning-and-teaching-tilt/110853"
    soup = BeautifulSoup(get(link).text, 'html.parser')
    text = soup.get_text().lower().strip()
    counter = 0
    while(text.find(search) == -1 and counter < 500):
        lines = [x.get('href') for x in soup.find_all('a')]
        random = rand.choice(lines)
        try:
            link = "https://en.wikipedia.org/" + random
        except TypeError:
            raise Exception("Idiot")
        start = get(link).text
        soup = BeautifulSoup(get(link).text, 'html.parser')
        text = soup.get_text().lower().strip()
        counter += 1
        sys.stdout.write(str(counter) + ", ")
        sys.stdout.flush()
        # print(link)
    else:
        print("Found {} at {} in {} tries.".format(search, link, counter))

if __name__ == "__main__":
    main()