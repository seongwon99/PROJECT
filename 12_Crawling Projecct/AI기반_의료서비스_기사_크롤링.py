# -*- encoding: utf-8 -*-
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# ---------------------------------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
def main(body):
    results=[]
    for n in body:
        results.append(n.text)
    results=''.join(results)
    results=results.replace("\xa0",'').replace("\r",'').replace("\n",'').replace("\t",'')
    return results

###############################################################
# AI기반 의료 서비스와 관련된 기사 크롤링
# 각각 다른 뉴스 사이트를 크롤링하기 때문에 개별의 크롤링 코드 작성
###############################################################

# # 1
url1='https://www.koit.co.kr/news/articleView.html?idxno=109838'
html1=urlopen(url1)
soup1=BeautifulSoup(html1.read(), 'html.parser')
main_1=soup1.select('div#article-view-content-div > p') # 본문1
main1=main(main_1)
header1=soup1.select_one('div.article-head-title').text # 헤더1

# 2
url2='http://www.bosa.co.kr/news/articleView.html?idxno=2111415'
html2=urlopen(url2)
soup2=BeautifulSoup(html2.read(), 'html.parser')
main_2=soup2.select('div#snsAnchor > div') # 본문 2
main2=main(main_2)
header2=soup2.select_one('header.article-view-header > h3.heading').text # 헤더2

# # 3
url3='https://www.etri.re.kr/webzine/20211112/sub01.html'
html3=urlopen(url3)
soup3=BeautifulSoup(html3.read(), 'html.parser')
main_3=soup3.select('p.txt0') # 본문1
main3=main(main_3)
header3=soup3.select_one('p.des').text # 헤더1

# # 4
url4='http://www.clinicjournal.co.kr/news/article.html?no=8711'
html4=urlopen(url4)
soup4=BeautifulSoup(html4.read(), 'html.parser')
main_4=soup4.select(' p') # 본문1
main4=main(main_4)
header4=soup4.select_one('div.art_top > h2').text # 헤더1

# 5
url5='https://www.medifonews.com/mobile/article.html?no=179929'
html5=urlopen(url5)
soup5=BeautifulSoup(html5.read(), 'html.parser')
main_5=soup5.select('div.news_detail > div') # 본문1
main5=main(main_5)
header5=soup5.select_one('div.news_top.mov_fix > h3').text # 헤더1

# 6
url6='https://www.bloter.net/news/articleView.html?idxno=27820'
html6=urlopen(url6)
soup6=BeautifulSoup(html6.read(), 'html.parser')
main_6=soup6.select('#article-view-content-div > p') # 본문1
main6=main(main_6)
header6=soup6.select_one('#article-view > div > header > h1').text # 헤더1

# 7
url7='https://www.koit.co.kr/news/articleView.html?idxno=111028'
html7=urlopen(url7)
soup7=BeautifulSoup(html7.read(), 'html.parser')
main_7=soup7.select('#article-view-content-div > p') # 본문1
main7=main(main_7)
header7=soup7.select_one('div.article-head-title').text # 헤더1

# 8
url8='http://www.monews.co.kr/news/articleView.html?idxno=319828'
html8=urlopen(url8)
soup8=BeautifulSoup(html8.read(), 'html.parser')
main_8=soup8.select('#article-view-content-div > p') # 본문1
main8=main(main_8)
header8=soup8.select_one('#article-view > div > header > h3').text # 헤더1

# 9
url9='http://www.thebell.co.kr/free/content/ArticleView.asp?key=202306212104116640108628'
html9=urlopen(url9)
soup9=BeautifulSoup(html9.read(), 'html.parser')
main_9=soup9.select('div.viewSection') # 본문1
main9=main(main_9)
header9=soup9.select_one('div.viewHead > p').text # 헤더1

import requests
# 10
url10='https://www.boannews.com/media/view.asp?idx=91852&kind=3'
html10=requests.get(url10, verify=False)
soup10=BeautifulSoup(html10.text, 'html.parser')
main_10=soup10.select('div#news_content') # 본문1
main10=main(main_10)
header10=soup10.select_one('#news_title02 h1').text # 헤더1

# 11
url11='http://www.seminartoday.net/news/articleView.html?idxno=11558'
html11=urlopen(url11)
soup11=BeautifulSoup(html11.read(), 'html.parser')
main_11=soup11.select('div#article-view-content-div > p') # 본문1
main11=main(main_11)
header11=soup11.select_one('div.article-head-title').text # 헤더1

# 12
url12='https://www.digitaltoday.co.kr/news/articleView.html?idxno=482567'
html12=urlopen(url12)
soup12=BeautifulSoup(html12.read(), 'html.parser')
main_12=soup12.select('article#article-view-content-div > p') # 본문1
main12=main(main_12)
header12=soup12.select_one('header.article-view-header > h3.heading').text # 헤더1

# # 13
url13='http://www.phidigital.co.kr/board/bbs_list.php?boardT=v&board_data=aWR4PTkmc3RhcnRQYWdlPTAmbGlzdE5vPTImdGFibGU9Y3NfYmJzX2RhdGEmY29kZT1wcmVzcyZzZWFyY2hfaXRlbT0mc2VhcmNoX29yZGVyPQ==%7C%7C&search_items=Y29kZT1wcmVzcyZzZWFyY2hfaXRlbT0mc2VhcmNoX29yZGVyPSZ1bnNpbmdjb2RlMT0mdW5zaW5nY29kZTI9JmNhdGU9JnB3ZD0=%7C%7C'
html13=urlopen(url13)
soup13=BeautifulSoup(html13.read(), 'html.parser')
main_13=soup13.select('div.board-content > span') # 본문1
main13=main(main_13)
header13=soup13.select_one('div.board-content > h2').text # 헤더1


# 헤더 데이터 리스트에 추가
header_List=[]
header_List.extend([header1,header2,header3,header4,header5,header6,header7,header8,header9,header10,header11,header12,header13])
for a in range(len(header_List)):
        header_List[a]=header_List[a].replace('\r','').replace('\t','').replace('\n','').replace('\xa0','')
# print(header_List)


# 본문 데이터 리스트에 추가
main_List=[]
main_List.extend([main1,main2,main3,main4,main5,main6,main7,main8,main9,main10,main11,main12,main13])


# 헤더와 본문 데이터 리스트에 추가
total=[]
for i in range(len(header_List)):
    row=[header_List[i], main_List[i]]
    total.append(row)
# print(total)


# 데이터 프레임 생성 
import pandas as pd
DF=pd.DataFrame(total,columns=['header','main'])

DF.to_csv('DF.csv', index=False,encoding='utf-8-sig')

# DF.to_csv('DF.txt',index=False,header=None)