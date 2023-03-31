# WebCrawling_kyochon-store
## 교촌치킨 매장 데이터 웹크롤링

정적 크롤링이란?
웹 페이지를 가져와서 한 페이지 안에서 원하는 정보가 모두 드러나는 정적인 데이터를 추출해 내는 방법

사용한 패키지:
BeautifulSoup - html 파싱
urllib.request - html 문서 가져올 때 필요
pandas - 데이터를 데이터프레임으로 만들 때 필요


### kyochon 크롤링
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

result = []

## 정적 크롤링 방법
# 서울, 부산, 대구, 인천, 광주, 울산, 세종, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주 순으로 sido2에 해당하는 페이지 수를 리스트로 나타냄
page_list = [25, 16, 8, 10, 5, 5, 5, 16, 44, 18, 15, 17, 15, 22, 24, 22, 2]

![image](https://user-images.githubusercontent.com/37770999/229093746-aaddffca-ec31-4959-8826-4d80f1267eba.png)
위 사진을 보면 교촌치킨 매장찾기 url의 경우 쉽게 마지막 페이지를 찾을 수 있는 구조가 아니었고 (시/도) 버튼을 클릭하고 스크롤을 내려서 각 (시/도)에 해당하는 (시/구/군)의 페이지를 다시 불러와야지 매장을 확인할 수 있는 구조이다.
그래서 각 (시/도) 당 페이지 수를 직접 세서 리스트에 저장


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
            
            
find_all: 기준에 맞는 태그를 모두 추출   /   find: 조건을 만족하는 태그 하나만 추출   /   select: 여러 옵션을 사용해 원하는 데이터 추출            
            

kyochon_tbl = pd.DataFrame(result, columns = ('store', 'sido', 'gungu', 'store_address'))
kyochon_tbl.to_csv("C:/Users/ksc/Desktop/web_crawling/kyochon_store.csv", encoding = "cp949", mode = "w", index = True)
