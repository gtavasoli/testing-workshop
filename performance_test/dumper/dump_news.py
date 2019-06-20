import requests
from bs4 import BeautifulSoup as bs
from time import sleep

pattern = 'https://www.mashreghnews.ir/page/archive.xhtml?wide=0&ms=0&pi={}'


def get_page_content(page_number):
    page = requests.get(pattern.format(page_number))
    if page.status_code == 200:
        return page.content
    else:
        return None


if __name__ == '__main__':
    max_page = 30

    with open("./news.csv", 'w') as f:
        for i in range(0, max_page):
            content = get_page_content(i)

            soup = bs(content, 'html.parser')

            for li in soup.select('li.news'):
                try:
                    title = li.select_one('h3').select_one('a').get_text()
                    brief = li.select_one('p').get_text()
                    print(title)
                    print(brief)
                    f.write('{},{}\n'.format(title, brief))
                except Exception as e:
                    pass  # Silly
            sleep(2)
