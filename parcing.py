import requests
import time
import random
import sqlite3
from bs4 import BeautifulSoup
price_list = []
name_list = []
for i in range(1,6):
    url = f'https://alta.ge/notebooks-page-{i}.html'
    info = requests.get(url)
    con = info.text
    soup = BeautifulSoup(con,'html.parser')
    lpt = soup.find_all('span', {'class': "ty-price-num"})
    nm = soup.find_all('a', {'class': 'product-title'})
    for each in range(len(lpt)):
        price_list.append(lpt[each].text)
        name_list.append(nm[each].text)
    time.sleep(random.randint(15, 20))

conn = sqlite3.connect("alta.sqlite")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE notebook
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                laptop VARCHAR,
                price varchar );''')

for a in range(len(price_list)):
    cursor.execute('INSERT INTO notebook (laptop, price) VALUES (?, ?)',
                   (name_list[a], price_list[a],))
    conn.commit()