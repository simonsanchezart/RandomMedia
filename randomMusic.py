import sys
import random
import requests
import bs4
import webbrowser
import time

amount = int(sys.argv[1])
openItems = sys.argv[2]

class MusicItem():
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def GetName(self):
        return self.name

    def GetLink(self):
        return self.link

def GetRequest():
    while(True):
        itemIndex = random.randint(1, 16500000)
        site = "https://www.discogs.com/release/" + str(itemIndex)

        re = requests.get(site)
        if re.status_code == 200:
            soup = bs4.BeautifulSoup(re.text, 'html.parser')

            itemTitle = soup.title.text.split(" -")[0]
            itemLink = re.request.url

            validItem = MusicItem(itemTitle, itemLink)
            break
    return validItem

links = []
for i in range(amount):
    validMusic = GetRequest()

    links.append(validMusic.GetLink())
    print(f"{validMusic.GetName()}")

if openItems.lower() == 'y':
    for link in links:
        webbrowser.open_new_tab(link)
        time.sleep(0.5)