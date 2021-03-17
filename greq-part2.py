from bs4 import BeautifulSoup
import grequests
import pandas as pd

def get_urls():
    urls = []
    for x in range(1,11):
        urls.append(f'https://www.canoeandkayakstore.co.uk/collections/activity-recreational-beginner?page={x}')
    return urls

def get_data(urls):
    reqs = [grequests.get(link) for link in urls]
    resp = grequests.map(reqs)
    return resp

def parse(resp):
    productlist = []
    for r in resp:
        sp = BeautifulSoup(r.text, 'lxml')
        items = sp.find_all('div', {'class': 'product-grid-item__info'})
        for item in items:
            product = {
            'title' : item.find_all('a')[0].text.strip(),
            'price': item.find('span', {'class': 'product-grid-item-price'}).find_all('span')[0].text.strip(),
            'avail': item.find('span', {'class': 'product-grid-item__info__availability--value'}).text.strip(),
            }
            productlist.append(product)
            print('Added: ', product)
    return productlist


urls = get_urls()
resp = get_data(urls)
df = pd.DataFrame(parse(resp))
df.to_csv('canoes.csv', index=False)
