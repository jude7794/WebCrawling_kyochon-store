### kyochon 크롤링
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

result = []

### 최대 페이지 수 탐색
# for sido in range(1,18):
#     tag_select = soupkyochon.find_all('select', attrs = {'id': 'sido2'})
#     print(tag_select)
#     # tag_option = tag_select.find_all('option')
#     # print(tag_option)

## 정적 크롤링 방법
# 서울, 부산, 대구, 인천, 광주, 울산, 세종, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주 순으로 sido2에 해당하는 페이지 수를 리스트로 나타냄
page_list = [25, 16, 8, 10, 5, 5, 5, 16, 44, 18, 15, 17, 15, 22, 24, 22, 2]

for sido1 in range(1, len(page_list)+1):
    for sido2 in range(1, page_list[sido1-1]+1):
        kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' %(sido1, sido2)
        # print(kyochon_url)
        html = urllib.request.urlopen(kyochon_url)
        soupkyochon = BeautifulSoup(html, 'html.parser')
        tag_ul = soupkyochon.find('ul', attrs = {'class': 'list'})
        # print(tag_ul)
        for store in tag_ul.find_all('span'):
            # print(store)
            if len(store) == 0:
                break
            store_name = store.find('strong').string
            store_em = store.find('em').text.split('\n')
            store_address = store_em[1].strip("\t""\r")   # 문자열 양 끝에 필요없는 \t, \r 제거
            store_sido = store_address.split()[0]   # store_address를 공백으로 나눈 것에서 0번째 단어
            store_gungu = store_address.split()[1]
            result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

# print(result)
# print(len(result))
kyochon_tbl = pd.DataFrame(result, columns = ('store', 'sido', 'gungu', 'store_address'))
kyochon_tbl.to_csv("C:/Users/ksc/Desktop/web_crawling/kyochon_store.csv", encoding = "cp949", mode = "w", index = True)


















