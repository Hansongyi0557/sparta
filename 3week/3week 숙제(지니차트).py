import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)
#print(data.text)  # get으로 받아온 정보를 data에 넣고, data의 내용을 html 코드로 보여줌


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#select 이용해서 테이블 안에 제목 불러오기
musics = soup.select('table.list-wrap > tbody > tr> td')
rank=0
# musics (td들) 의 반복문을 돌리기
for music in musics:
    title_el = music.select('a.title.ellipsis') #a태그만 찾기
    singer_el = music.select('a.artist.ellipsis') #a태그만 찾기
    if len(title_el) > 0: # title_el의 길이가 0보다 크면
        rank +=1
        title = title_el[0].text
        singer = singer_el[0].text
        print(rank,title,singer)
