import sys
import random
import requests
import bs4
import webbrowser
import time

amount = int(sys.argv[1])
movieOrShow = sys.argv[2]
openItems = sys.argv[3]
scoreThreshold = float(sys.argv[4])

class CinemaItem():
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
        if movieOrShow == 'm':
            itemIndex = random.randint(1, 800000)
            site = "https://www.themoviedb.org/movie/" + str(itemIndex)
        elif movieOrShow == 's':
            itemIndex = random.randint(1, 89000)
            site = "https://www.themoviedb.org/tv/" + str(itemIndex)

        re = requests.get(site)
        if re.status_code == 200:
            soup = bs4.BeautifulSoup(re.text, 'html.parser')

            itemTitle = soup.title.text.split(' —')[0]
            itemScoreAttributes = soup.find("div", class_="user_score_chart").attrs
            itemScore = float(itemScoreAttributes["data-percent"])
            itemLink = re.request.url

            if itemScore >= scoreThreshold:
                validItem = CinemaItem(itemTitle, itemLink, itemScore)
                break
    return validItem

links = []
for i in range(amount):
    validCinemaItem = GetRequest()

    links.append(validCinemaItem.GetLink())
    print(f"{validCinemaItem.GetName()} - {validCinemaItem.GetScore()}%")

if openItems.lower() == 'y':
    for link in links:
        webbrowser.open_new_tab(link)
        time.sleep(0.5)