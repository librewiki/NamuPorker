__author__ = 'seyriz'
from urllib.request import *
from urllib.error import *
from urllib.parse import *
from sys import  argv
from os import path, mkdir
import time

class porker(object):
    def __init__(self):
        self.namu = "https://namu.wiki/raw/"
        # self.document = argv[1]
        self.document = "SCP 재단"
        self.document_urlencoded = quote(self.document)
        self.headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        self.pork()

    def pork(self):
        if(not path.exists(self.document)):
            mkdir(self.document)
        url = self.namu + self.document_urlencoded + "?rev="
        rev = 1
        while(True):
            try:
                print("rev : ", rev)
                if(path.exists(self.document+"/"+str(rev)+".namu")):
                    pass
                else:
                    req = Request(url=url+str(rev), headers=self.headers)
                    response = urlopen(req)
                    html = response.read().decode()
                    try:
                        if(html.index("g-recaptcha") > 0):
                            print("Too many request ERROR")
                            break
                    except :
                        pass
                    f = open(self.document+"/"+str(rev)+".namu", mode='w')
                    f.write(html)
                    f.close()
                    time.sleep(3)
                rev += 1
            except HTTPError as e:
                print(e)
                break


if(__name__ == "__main__"):
    porker()