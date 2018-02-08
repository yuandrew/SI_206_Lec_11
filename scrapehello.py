#scrapehello.py

from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())


# searching by class
all_goodbye_elements = soup.find_all(class_='goodbye')
goodbye_elements_list = soup.find_all('li')
# all_french_list_items = soup.find_all('li', class_='french')
# print(all_goodbye_elements)
for element in goodbye_elements_list:
    print(element.string)
img_tag = soup.find('img')
print(img_tag['width'])
url_tag = soup.find('a')
print(url_tag['href'])
