""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.
1) kas ir rss?
-  really simple sintication ir tehnologija kas lauj sekot jaunakajiem notikumiem saturam, dazados resursos
    1- jaunumi un saturs
    2 -agregatori- sistema kas lauj abonet interesejosos avotus

2) ko nozīmē plūsmu no google.lv?
- google ir vietne, bet nav satura radītājā, ta izmanto rss


pip install feedparser

...pip upgrade ...
"""

import feedparser

# define URL uz RSS plūsmu

rss_url='https://news.google.com/home?hl=lv&gl=LV&ceid=LV:lv'

#iegūst RSS plūsmas datus un veicam analīzi..

kkk=feedparser.parse(rss_url)

#noformēšana
for entry in kkk.entries:
    print("Virsraksts", entry.title)
    print("Saite", entry.link)
    print("Publicēšanas datums", entry.published)
    print("\n")  #jaunās rindas simbols html \ tatad parcelts uz nakamo rindu



