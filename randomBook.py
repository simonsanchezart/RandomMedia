import sys
import random
import requests
import bs4
import webbrowser
import time

amount = int(sys.argv[1])
openItems = sys.argv[2]
scoreThreshold = float(sys.argv[3])

class BookItem():
    def __init__(self, name, link, score):
        self.name = name
        self.link = link
        self.score = score

    def GetName(self):
        return self.name

    def GetLink(self):
        return self.link

    def GetScore(self):
        return self.score

def GetRequest():
    while(True):
        itemIndex = random.randint(1, 55000000)
        site = "https://www.goodreads.com/book/show/" + str(itemIndex)

        re = requests.get(site)
        if re.status_code == 200:
            soup = bs4.BeautifulSoup(re.text, 'html.parser')

            itemTitle = soup.title.text
            itemScoreElement = soup.find("span", {"itemprop":"ratingValue"})
            itemScore = float(itemScoreElement.text)
            itemLink = re.request.url

            if itemScore >= scoreThreshold:
                validItem = BookItem(itemTitle, itemLink, itemScore)
                break
    return validItem

links = []
for i in range(amount):
    validBook = GetRequest()

    links.append(validBook.GetLink())
    print(f"{validBook.GetName()} - {validBook.GetScore()}/5.0")

if openItems.lower() == 'y':
    for link in links:
        webbrowser.open_new_tab(link)
        time.sleep(0.5)
