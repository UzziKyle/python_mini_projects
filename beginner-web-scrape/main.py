# A program that prints a list of articles found on the homepage of Palawan News and their respective links

# Putangina, ang sakit sa mata ng documentation ng BeautifulSoup ta's sumasabay pa kalutangan ko    
# Namahinga na lang sana ako para hindi ganitong ka-inefficient 
# Took me more than an hour. It's better than nothing tho


import requests
from bs4 import BeautifulSoup as bs

url = "https://palawan-news.com/"

r = requests.get(url)

r_html = r.text

soup = bs(r_html, features='lxml')

article_titles = soup.find_all('h3', class_='entry-title')

print("Here is a list of articles on the Palawan News homepage:")

num = 1
for title in article_titles:
    link = title.find('a').get('href')
    print("{}.\t{}\nLink:\t{}\n".format(num, title.text, link))
    num += 1