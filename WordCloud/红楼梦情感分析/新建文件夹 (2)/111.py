import urllib
import re
from bs4 import BeautifulSoup as bs

book = []
for i in range(120):
    print("处理第{}回...".format(i+1))
    if i+1<10:
        url = "http://www.purepen.com/hlm/00{}.htm".format(i+1)
    elif i+1 < 100:
        url = "http://www.purepen.com/hlm/0{}.htm".format(i+1)
    else:
        url = "http://www.purepen.com/hlm/{}.htm".format(i+1)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    bsObj = bs(response.read().decode('gb18030')) #注意原网页的codec是哪一种
    chapter = bsObj.table.font.contents[0]
    book.append(chapter)
