from bs4 import BeautifulSoup
import requests
import csv

access1 = requests.get('https://www.wikipedia.org/')
page_1 = BeautifulSoup(access1, 'lxml')
my_page = page_1.find_all('a', 'title')
print(my_page.text)

# id="js-link-box-de" href="//de.wikipedia.org/" title="Deutsch — Wikipedia — Die freie Enzyklopädie"