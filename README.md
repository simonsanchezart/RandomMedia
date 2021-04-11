# RandomCinema

Requirements:
---
pip install beautifulsoup4

Usage:
---
randomCinema.py amount type openItems scoreThreshold
randomBook.py amount openItems scoreThreshold
randomMusic.py amount openItems

amount - Number of random items to get

type - 'm' for movies, 's' for tv shows, without quotes

openItems - 'y' to open links in browser, 'n' to not open link in browser, without quotes

scoreThreshold - number between 0 and 100 for cinema, between 0 and 5 for books, will only get movies/shows with equal or higher score than the threshold
