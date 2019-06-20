import requests
from bs4 import BeautifulSoup as bs

pattern = 'https://www.mashreghnews.ir/page/archive.xhtml?wide=0&ms=0&pi={}'


def get_page_content(page_number):
    page = requests.get(pattern.format(page_number))
    if page.status_code == 200:
        return page.content
    else:
        return None


if __name__ == '__main__':
    content = get_page_content(1)
    soup = bs(content, 'html.parser')

    for li in soup.select('li.news'):
        print(li.select_one('h3').select_one('a').get_text())
        print(li.select_one('p').get_text())


