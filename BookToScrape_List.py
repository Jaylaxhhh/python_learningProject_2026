# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:26:35 2026

@author: Jay
"""
import requests
#import re
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def NavigateToNewUrl(book_category,start_url,html):
    soup = BeautifulSoup(html,"html.parser")
   # a_tag = soup.find("a", string=lambda t: t and t.strip() == book_category)
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        if text == book_category:
            a_tag = a
            break
        
    if a_tag:
        href = a_tag["href"]
      #  print("原始href：", href)
        # 注意：网站是相对链接，拼接完整url
        from urllib.parse import urljoin
        full_url = urljoin(start_url, href)
     #   print("完整链接：", full_url)
        return full_url
    

def parsePage(book_list,html):
    new_soup = BeautifulSoup(html,"html.parser")
    for article in new_soup.find_all('article'):
        book_name = article.h3.a["title"]
        price = article.find("p", class_="price_color").get_text(strip=True)
        if not book_name or not price:
            continue  
        
        book_list.append([book_name,price])

def printBookList(ilt):
    tplt = "{:^8}\t{:40}\t{:^8}"
    print(tplt.format("序号","书名","价格"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count,g[0],g[1]))
    
def main():
    book_category = "Music"
    start_url = "https://books.toscrape.com/index.html"
    Book_lt = []

    Full_url = ""
    html_txt = getHTMLText(start_url)
    Full_url = NavigateToNewUrl(book_category,start_url,html_txt)
    html_content = getHTMLText(Full_url)    
    parsePage(Book_lt,html_content)
    printBookList(Book_lt)

main()


'''
for test in soup.find_all('a'):
    if test.string != None :
        print(test.string)
    else:
        continue
'''         