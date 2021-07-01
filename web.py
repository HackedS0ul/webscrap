from bs4 import BeautifulSoup
import requests
import time
import csv



cookies ={
    'CSRF-TOKEN': 'db4e9a62-9d20-4661-a960-76d83be39dc4',

}
headers = {
    'method': 'GET',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection':'close',
    'Host': 'ls.hit.gemius.pl',
    'Upgrade-Insecure-Requests':'1',
    'Sec-Fetch-Site': 'cross-site',

    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'iframe',

    'Referer': 'https://allegro.pl/',

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
#url ='https://allegro.pl/uzytkownik/123lazienka/kabiny-i-prysznice-kabiny-prysznicowe-253705?ksztalt=kwadratowy&bmatch=e2101-d3794-c3683-hou-1-5-0616'
#r = requests.get(url, headers=headers, cookies=cookies)
#print(r.status_code)
#soup = BeautifulSoup(url.content, 'lxml')
'''
products = soup.find('div', class_='_9a071_1hu0a _1bo4a _xu6h2 _m7qxj _9a071_Em-aO')
for product in products:
    product_name = soup.find('h1', class_='_1s2v1 _1djie _4lbi0')
    product_price = soup.find('div', class_='_1svub _lf05o _9a071_3SxcJ')
    product_description = soup.find('div', class_='_2d49e_5pK0q')
    print('Product name: ', product_name.text.strip())
    print('Product Price: ', product_price.text.strip())
    print('Product Description: ', product_description.text.strip())
'''
for i in range(1,3):
    r = requests.get('http://allegro.pl/uzytkownik/123lazienka/kabiny-i-prysznice-kabiny-prysznicowe-253705?ksztalt=kwadratowy&bmatch=e2101-d3794-c3683-hou-1-5-0616&p={i}', headers=headers, cookies=cookies)
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
    myImage = soup.find_all('img', class_='_b8e15_2LNko',src=True)
    productname = soup.find('h1', class_='_1s2v1 _1djie _4lbi0').text.strip()
    product_price = soup.find('div', class_='_1svub _lf05o _9a071_3SxcJ').text.strip()
    product_description = soup.find('div', class_='_2d49e_5pK0q').text.strip()
    productImages = []
    for image in myImage:
        productImages.append(image['src'] + str('.jpg'))

    urls = {
        'Product name': productname,
        'Product Price': product_price,
        'Product Description': product_description,
        'product Images': productImages,
    }
    
    url_list.append(urls)
    print('Adding product:', urls['Product name'])
    with open ('fileq.csv','w', encoding='utf-8') as file:
        writer=csv.writer(file)
        for row in url_list:
            
            writer.writerow(['Name:\n',row['Product name'],'Price:', row['Product Price'], 'Description:\n', row['Product Description'],'images:\n', row['product Images']])

