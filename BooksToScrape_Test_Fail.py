# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:03:36 2026

@author: Jay
"""
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def parsePage(ilt,html):
    try:
        plt = re.findall(,html)
        tlt = re.findall(,html)
    
    
    print("")
    
def printGoodsList(ilt):
    print("")
    
def main():
    book_category = "fiction"
    depth = 2
    start_url = 'https://books.toscrape.com/index.html'
    start_url = 'https://books.toscrape.com/catalogue/category/books/business_35/index.html'
    infoList = []
    for i in range(depth):
        try:
            url = start_url +"&s=" + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    
main()
