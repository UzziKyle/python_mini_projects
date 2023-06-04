# A program that prints a list of articles found on the homepage of Palawan News and their respective links

# Putangina, ang sakit sa mata ng documentation ng BeautifulSoup ta's sumasabay pa kalutangan ko  
# Try viewing this "https://www.crummy.com/software/BeautifulSoup/bs4/doc/" 
# Namahinga na lang sana ako para hindi ganitong ka-inefficient 
# Took me more than an hour. It's better than nothing tho


import requests
from bs4 import BeautifulSoup as bs

url = "https://palawan-news.com/"

page = requests.get(url)

page_html = page.text

soup = bs(page_html, features='lxml')

article_titles = set(soup.find_all('h3', class_='entry-title'))


print("Here is a list of articles on the Palawan News homepage:")

num = 1
raw_article_titles = [[title.text, title.find('a').get('href')] for title in article_titles]
sorted_article_titles = sorted(raw_article_titles)

for title in sorted_article_titles:
    print("{}.\t{}\nLink:\t{}\n".format(num, title[0], title[1]))
    num += 1
