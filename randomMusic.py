import random
import webbrowser
import argparse

parser = argparse.ArgumentParser(description="Show random items from Discogs")
parser.add_argument("-amount", metavar="amount", default=10, type=int, help="Enter the amount of items to be selected")
args = parser.parse_args()

for _ in range(args.amount):
    link = "https://www.discogs.com/release/" + str(random.randint(0, 9999999))
    webbrowser.open_new_tab(link)