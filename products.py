from bs4 import BeautifulSoup
import requests
import time
import csv


headers = {
    'authority': 'allegro.pl',
    'method': 'GET',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,en-US;q=0.9,lt;q=0.8,la;q=0.7,vi;q=0.6,nl;q=0.5',
    'cache-control': 'max-age=0',
    'dpr': '1.25',
    'upgrade-insecure-requests': '1',
    'cookie':'_cmuid=939c3ed5-f92c-454c-9a88-56399f10e02f; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; gdpr_permission_given=1; datadome=SYZSrbGyg9FlPN3HMJZKSfTPJg3doyNM7wc_H7FilGEEAC0zkLMBrnTMff2s.Z2ja7Tcp2h5Lr7y-oEa7zAqMqvye0aeiKYNR2kD20XVHX',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    } 

#re = requests.get('https://allegro.pl', headers=headers)
#print(re.status_code)
url="https://allegro.pl/kategoria/lazienka-i-toaleta-baterie-lazienkowe-46128?bmatch=e2101-d3858-c3683-hou-1-3-0429p={i}"
soup = BeautifulSoup(url.content, 'lxml')

products = soup.find('div', class_='_9a071_1hu0a _1bo4a _xu6h2 _m7qxj _9a071_Em-aO')
for product in products:
    product_name = soup.find('h1', class_='_1s2v1 _1djie _4lbi0')
    product_price = soup.find('div', class_='_1svub _lf05o _9a071_3SxcJ')
    product_description = soup.find('div', class_='_2d49e_5pK0q')
    print('Product name: ', product_name.text.strip())
    print('Product Price: ', product_price.text.strip())
    print('Product Description: ', product_description.text.strip())

for i in range(1,3):
    r = requests.get('https://allegro.pl/kategoria/lazienka-i-toaleta-baterie-lazienkowe-46128?bmatch=e2101-d3858-c3683-hou-1-3-0429p={i}', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    product = soup.find_all('article', class_='mx7m_1 mnyp_co mlkp_ag')
    product_links = []

    for item in product:
        for link in item.find_all('a', href=True):
            product_links.append(link['href'])

url_list = []
for url in product_links:
    test = requests.get(url, headers=headers)
    soup = BeautifulSoup(test.content, 'lxml')
    productname = soup.find('table', class_='wikitable.sortable.jquery-tablesorter')

    urls = {
        'Product name': productname,
    }
    
    url_list.append(urls)
    print('Adding names:', urls['Product name'])
    with open ('vls.csv','w', encoding='utf-8', newline='') as file:
        writer=csv.writer(file)
        for row in url_list:
            
            writer.writerow(['Name:\n',row['Product name']])

