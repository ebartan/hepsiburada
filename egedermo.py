import requests
from bs4 import BeautifulSoup
import gspread
import datetime
import csv

asins = []

with open('egedermo.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        asins.append(row[0])
print(asins)


for asin in asins:
    def request():
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; rv:79.0) Gecko/20100101 Firefox/79.0'}
        r = requests.get(f'https://www.egedermo.com/urun/{asin}', headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup

    def parse(soup):
        baslik = soup.find('div',{'class' : 'product-title'}).text.strip().split('\t')[0]
        price = soup.find('div',{'class' : 'product-price-old'}).text.strip().split('\t')[0]

        product = {'baslik': baslik, 'price': price}
        return product

    def output(product):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('egedermowebscraping').sheet1
        sh.append_row([ str(product['baslik']),str(product['price'])  ], table_range='D3')
        return

    data = request()
    product = parse(data)
    output(product)
    print(product)
