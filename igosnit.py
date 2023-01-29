import requests as req
from bs4 import BeautifulSoup as btu
import random
from colorama import Fore, Style
import json
print(Fore.WHITE+Style.BRIGHT +""" 
 ___                                   _               
  |  ._   _ _|_  _.  _  ._ _. ._ _    / \  _ ._  o _|_ 
 _|_ | | _>  |_ (_| (_| | (_| | | |   \_/ _> | | |  |_ 
                     _|                                
Beta Sürümü 1.v
""")
user = input("user name: ")
class instagram:
    def __init__(self):
        self.url = f"http://www.instagram.com/{user}"
        self.usert =  ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
    
    
    def instagramOsnit(self):
        istek = req.get(self.url, headers={'User-Agent': random.choice(self.usert)})
        html = istek.text
        soup = btu(html, "html.parser")
        soup.encode('utf-8')
        data = soup.find_all('meta', attrs={'property': 'og:description'})      
        for i in data:
            followers = i.get("content").split(",")[0].strip()
            following = i.get("content").split(",")[1].strip()
            post = i.get("content").split(",")[2].strip().split("-")[0]
        print(Fore.GREEN+ Style.BRIGHT + "User:"+Fore.WHITE+user)
        print(Fore.GREEN+ Style.BRIGHT + "following:"+Fore.WHITE+following)
        print(Fore.GREEN + Style.BRIGHT + "follwers:"+Fore.WHITE+followers)
        print(Fore.GREEN + Style.BRIGHT + "post:"+Fore.WHITE+post)

if __name__=="__main__":
       app = instagram()
       app.instagramOsnit()
        