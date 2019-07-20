import requests
from bs4 import BeautifulSoup
import uuid
import sys
import os
import magic
def downloader(url):
    mimetype=magic.Magic()
    liste=[]
    if str(url).startswith("https://www.cheatography.com") or str(url).startswith("http://www.cheatography.com"):
        req=requests.get(str(url))
        sp=BeautifulSoup(req.content,"html.parser")
        href=sp.find_all('a')
        for i in href:
            a=i.get("href")
            if "/cheat-sheets/" in str(a):
                liste.append(str(a))
        liste=set(liste)
        print(str(len(liste)))
    for sheet in liste:
        sheet="http://www.cheatography.com"+sheet+"pdf/"
        pdf=requests.get(sheet)
        filename=str(uuid.uuid4().hex[:8])
        f=open(filename+".pdf","wb")
        f.write(pdf.content)
        f.close()
    #removing irrelevant pdf files
    files=os.listdir(str(os.getcwd()))
    for fl in files:
        if str(fl).endswith(".pdf"):
            mime=mimetype.from_file(str(fl))
            if "PDF" in str(mime):
                pass
            else:
                os.remove(str(os.getcwd())+"/"+str(fl))
downloader("http://www.cheatography.com/tag/"+sys.argv[1])