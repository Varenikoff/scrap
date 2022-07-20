import requests
from bs4 import BeautifulSoup
from pprint import pprint

HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')
result_list = list()

def parsing(ent):

    for element in ent:
        if any(w in element for w in KEYWORDS):
            title_element = article.find('a', class_='tm-article-snippet__title-link')
            title_result = title_element.text
            time_element = article.find('span', class_='tm-article-snippet__datetime-published')
            href = title_element['href']
            result = f'<{time_element.text}> - <{title_result}> - <{href}>'
            if result not in result_list:
                result_list.append(result)
            break


for article in articles:
    hubs = [w.text.strip().lower() for w in article.find_all(class_="tm-article-snippet__hubs-item")]
    titles = [w.text.strip().lower() for w in article.find_all('a', class_='tm-article-snippet__title-link')]
    posts_text = [w.text.strip().lower() for w in article.find_all('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2')]

    parsing(posts_text)
    parsing(titles)
    parsing(hubs)


pprint(result_list)