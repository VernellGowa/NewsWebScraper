import requests
from bs4 import BeautifulSoup


URL = "https://www.bbc.co.uk/news/uk"
page = requests.get(URL)
articles = []

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="gel-layout gel-layout--equal")
# print(results.text)

table = results.find_all("div" , 
class_=["gel-layout__item gs-u-pb+@m gel-1/3@m gel-1/4@xl gel-1/3@xxl nw-o-keyline nw-o-no-keyline@m",
"gel-layout__item gs-u-pb+@m gel-1/3@m gel0-1/4@xl gel-1/3@xxl nw-o-keyline nw-o-no-keyline@m"])


for item in table:
    heading = item.find("a").text
    text = item.find("p",).text
    
    articles.append([heading,text])

with open('articles.txt', 'w') as f:

    for article in articles:
        f.write(article[0] + "\n")
        f.write(article[1] + "\n")
        f.write("\n")


