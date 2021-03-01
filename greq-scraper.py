import grequests
from bs4 import BeautifulSoup
import time

def get_urls():
    urls = []
    for x in range(1,51):
        urls.append(f'http://books.toscrape.com/catalogue/page-{x}.html')
    return urls

def get_data(urls):
    reqs = [grequests.get(link) for link in urls]
    resp = grequests.map(reqs)
    return resp


def parse_data(resp):
    for r in resp:
        sp = BeautifulSoup(r.text, 'lxml')
        data = sp.find_all('article', {'class': 'product_pod'})
        for item in data:
            name = item.find('h3').text
            price = item.find('p', {'class': 'price_color'}).text
            print(name, price)
    return

if __name__ == '__main__':
    start = time.perf_counter()
    urls = get_urls()
    resp = get_data(urls)
    parse_data(resp)
    fin = time.perf_counter() - start
    print(fin)


# time taken 1.9101574999999684
