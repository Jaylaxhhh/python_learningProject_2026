# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:58:44 2026

@author: Jay
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:57:13 2026

@author: laxjay
"""

import requests
from bs4 import BeautifulSoup

#import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.status_code)
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find_all('tr'):
        rank_div = tr.find(class_="ranking")
        name_span = tr.find(class_="name-cn")
        if not rank_div or not name_span:
            continue    
        
        td_list = tr.find_all("td")
        rank = rank_div.get_text(strip=True)
        name = name_span.get_text(strip=True)
        total_score = td_list[4].get_text(strip=True)
        ulist.append([rank, name,total_score])   

def printUnivList(ulist,num):
    print("{:^10}\t{:^10}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^10}\t{:^10}".format(u[0],u[1],u[2]))
       #print("{:^10}\t{:^10}\t{:^10}".format(u[0],'qinghua','fen'))
    
def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2026"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 10)
main()
