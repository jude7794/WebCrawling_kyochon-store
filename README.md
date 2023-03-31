# WebCrawling_kyochon-store
## 교촌치킨 매장 데이터 웹크롤링

정적 크롤링이란?
웹 페이지를 가져와서 한 페이지 안에서 원하는 정보가 모두 드러나는 정적인 데이터를 추출해 내는 방법

사용한 패키지:  
BeautifulSoup - html 파싱  
urllib.request - html 문서 가져올 때 필요  
pandas - 데이터를 데이터프레임으로 만들 때 필요  

사용 함수:  
find_all: 기준에 맞는 태그를 모두 추출  
find: 조건을 만족하는 태그 하나만 추출  
select: 여러 옵션을 사용해 원하는 데이터 추출    


### kyochon 크롤링


![image](https://user-images.githubusercontent.com/37770999/229093746-aaddffca-ec31-4959-8826-4d80f1267eba.png)
위 사진을 보면 교촌치킨 매장찾기 url의 경우 쉽게 마지막 페이지를 찾을 수 있는 구조가 아니었고 (시/도) 버튼을 클릭하고 스크롤을 내려서 각 (시/도)에 해당하는 (시/구/군)의 페이지를 다시 불러와야지 매장을 확인할 수 있는 구조이다.
그래서 각 (시/도) 당 페이지 수를 직접 세서 리스트에 저장


### 결과
![image](https://user-images.githubusercontent.com/37770999/229097193-74c4abb5-2b41-4e0c-9751-57354186bed7.png)
이렇게 데이터프레임 csv 파일로 매장 크롤링 결과가 저장된다.


