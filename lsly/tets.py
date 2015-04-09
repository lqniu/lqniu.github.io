# -*- coding: utf-8 -*-  
import urllib2
import html5lib
import ConfigParser
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
href=[""]
title=[""]

def get_alllists():
    page=urllib2.urlopen(domain).read()
    soup=BeautifulSoup(page,"html5lib")
    zw=soup.findAll("a", rel="nofollow")
    for item in zw: 
        href.append(item['href'].encode('utf8'))
        title.append(item.text.encode('utf8'))

def get_text(index):
    ss=domain+href[index]
    page=urllib2.urlopen(ss).read()
    soup=BeautifulSoup(page,"html5lib")
    zw=soup.find("div",id="text_area")
    path="./text/"
    filename=path+'%03u'%(index)+title[index]+".txt"
    print filename.decode('utf-8').encode('gbk')
    fp=open(unicode(filename,"utf8"),'w')
    L=zw.text.encode('utf8')
    L1=L.split("    ")
    L2=L1[1:-1]
    fp.write(title[index]+'\n')
    for par in L2:
        fp.write(par+'\n')
    fp.close()
conf=ConfigParser.ConfigParser()
conf.read("config.ini")
domain=conf.get("global","domain")
newest=int(conf.get("global","newest"))
get_alllists()
print "total:"+str(len(title))
if newest<len(title):
    for index in range(newest,len(title)):
        get_text(index)
        newest=index+1
else:
    print "no new"
conf.set("global","newest",newest)
fcfp=open("config.ini",'w')
conf.write(fcfp)
fcfp.close()
    
