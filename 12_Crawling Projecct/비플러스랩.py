from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def main(body):
    results=[]
    for n in body:
        results.append(n.text)
    results=''.join(results)
    results=results.replace("\xa0",'').replace("\r",'').replace("\n",'').replace("\t",'')
    return results

###################################################################################################

urls=['https://beplushealthcare.com/newsroom/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=15532229&t=board',
      'https://beplushealthcare.com/newsroom/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=15437038&t=board',
      'https://beplushealthcare.com/newsroom/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=15212865&t=board',
      'https://beplushealthcare.com/newsroom/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6MTt9&bmode=view&idx=14582310&t=board',
      'https://beplushealthcare.com/newsroom/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6MTt9&bmode=view&idx=14582310&t=board',
      'https://beplushealthcare.com/newsroom/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6MTt9&bmode=view&idx=14970932&t=board']


header_List=[]
main_List=[]
total=[]

# 크롤링
for url in urls:
    html=urlopen(url)
    soup=BeautifulSoup(html.read(), 'html.parser')
    main_=soup.select('div.board_txt_area') # 본문1
    re_main=main(main_)
    header=soup.select_one('div.widget.board._list_wrap > div > div > div > header > p').text # 헤더1
    
    header_List.append(header)
    main_List.append(main)

    for a in range(len(header_List)):
            header_List[a]=header_List[a].replace('\r','').replace('\t','').replace('\n','').replace('\xa0','')

    for i in range(len(header_List)):
        row=[header_List[i], main_List[i]]
        total.append(row)



# 데이터프레임으로 저장
DF2=pd.DataFrame(total,columns=['header','main'])
DF2.to_csv('DF2.csv', index=False,encoding='utf-8-sig')