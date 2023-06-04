# A program that prints a list of articles found on the homepage of Palawan News and their respective links

# Putangina, ang sakit sa mata ng documentation ng BeautifulSoup ta's sumasabay pa kalutangan ko  
# Try viewing this, "https://www.crummy.com/software/BeautifulSoup/bs4/doc/" 
# Nagpahinga na lang sana ako para hindi ganitong ka-inefficient 
# Took me more than two hours. It's better than nothing tho


import requests
from bs4 import BeautifulSoup as bs

url = "https://palawan-news.com/"

page = requests.get(url)

page_html = page.text

soup = bs(page_html, features='lxml')

raw_article_titles = soup.find_all('h3', class_='entry-title') # Gets the necessary raw data from the webpage

filtered_article_titles = sorted([[title.text, title.find('a').get('href')]for title in set(raw_article_titles)]) # Removes duplicates and sorts titles alphanumerically

article_titles = [{'title': title, 'url': url} for title, url in filtered_article_titles] # Turns into a dictionary for easy data analysis

print("These are the articles on the Palawan News homepage:")
num = 1
for title in article_titles:
    print("{}.\t{}\nLink:\t{}\n".format(num, title["title"], title["url"]))
    num += 1
