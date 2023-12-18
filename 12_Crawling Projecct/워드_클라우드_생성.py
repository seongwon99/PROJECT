import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import platform
import matplotlib.pyplot as plt

text=open('DF.csv', encoding='utf-8-sig').read()
# print(text)

okt = Okt()
text_tag=[]
text_tag=okt.pos(text, norm=True, stem=False)

# print(text_tag)

noun_adj_list=[]
for word, tag in text_tag:
    if tag in ['Noun', 'Adjective']: # tag가 명사이거나 형용사인 단어들만 사용
        noun_adj_list.append(word)

# print(noun_adj_list)

counts=Counter(noun_adj_list)
tags=counts.most_common(100)

wc=WordCloud(font_path=r'C:/Users/KDP-48/Desktop/크롤링/malgun.ttf',background_color='white', max_font_size=60)
cloud=wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()