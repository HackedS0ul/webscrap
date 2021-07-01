from bs4 import BeautifulSoup
import requests
import time
import csv

proxies = {
  "https": "https://160.16.226.31:3128",
}
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
url ='http://allegro.pl/uzytkownik/123lazienka/kabiny-i-prysznice-kabiny-prysznicowe-253705?ksztalt=kwadratowy&bmatch=e2101-d3794-c3683-hou-1-5-0616'
r = requests.get(url, headers=headers, cookies=cookies)
print(r.status_code)
