#! python3
# downloadXkcd.py - загружает все комиксы XKCD

import requests, os, bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True) # создаем папку для сохранения комикса
while not url.endswith('#'):
    # загрузка страницы
    print('Загружается страница %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='lxml')

    # поиск url-адреса изображения
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалось найти изображение комикса.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # загрузка изображения
        print('Загружается изображение %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)

    # получение url-адреса кнопки Prev
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + prevLink.get('href')

print('Готово.')
