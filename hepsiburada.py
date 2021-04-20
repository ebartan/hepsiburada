import requests
from bs4 import BeautifulSoup
import gspread
import datetime

def request():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    url = 'https://www.hepsiburada.com/la-roche-posay-effaclar-gel-200-ml-effaclar-k-30-ml-set-p-HBV00000GHADU'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def parse(soup):
    baslik = soup.find('h1', {'class' : 'product-name best-price-trick'}).text.strip()
    price = soup.find('span', {'id' : 'offering-price'}).text.strip("\nTL").replace(',', '.')
    product = {'baslik': baslik, 'price': price,}
    return product


def output(product):
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open('egedermowebscraping').sheet1
    sh.append_row([ str(product['baslik']) , float(product['price'])])
    return


data = request()
product = parse(data)
output(product)
