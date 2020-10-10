import requests
from bs4 import BeautifulSoup as bs
import hashlib
import time

url="http://docker.hackthebox.eu:30950/"
ss=requests.Session()

for i in range(0,10):
    req=ss.get(url)
    soup = bs(req.content,'html.parser')
    
    str1=soup.h3.text
    str2=hashlib.md5(str1).hexdigest()

    print("Unhashed String: "+str1)
    print("Hashed String: "+str2)
    
    DATA = {'hash':str2}
    pst=ss.post(url,data=DATA)

    print("\n")
    print(pst.content)
    print("\n")


