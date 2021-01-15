#! python3
# lucky.py - открывает несколько результатов поиска с помощью Google

import requests, sys, webbrowser, bs4

print('Гуглим...') # отображается при загрузке страницы Google
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select(' .LC20lb DKV0Md a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
