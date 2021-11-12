
import socket
import time

#发送get请求获取文本文件
def SendReqGetText():
    mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

    mysock.send(cmd)

    while True:
        data=mysock.recv(512)
        if len(data)<1:
            break
        print(data.decode(),end=' ')
    mysock.close()


#发送Get请求获取并保存图片
def SendReqGetPic():
    host='data.pr4e.org'
    port=80
    count=0
    pic=b''
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect((host,port))
    mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

    while True:
        data=mysock.recv(5120)
        if len(data)<1:
            break
        count+=len(data)
        pic+=data
        print(len(data),count)
        time.sleep(0.25)

    mysock.close()

    #查找http头的结尾(\r\n\r\n)
    pos=pic.find(b'\r\n\r\n')
    print('heard length: ',pos)
    print(pic[:pos].decode())

    #跳过http头并保存图片
    pic=pic[pos+4:]
    fhand=open('cover.jpg',"wb")
    fhand.write(pic)
    fhand.close()

#SendReqGetPic()


#使用urllib获取文本文件
import urllib.request

def urllibGetText():
    fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

    for line in fhand:
        line=line.decode()
        line=line.strip()
        print(line)

#urllibGetText()


#使用urllib获取文本文件并计算单词频率
import urllib.request,urllib.parse,urllib.error

def urllibGetTextAndCalWords():
    fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

    counts=dict()
    for line in fhand:
        words=line.decode().split()
        for word in words:
            counts[word]=counts.get(word,0)+1
    print(counts)

#urllibGetTextAndCalWords()

def urllibGetPic():
    img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
    fhand=open('cover3.jpg','wb')
    fhand.write(img)
    fhand.close()

#urllibGetPic()

def urllibGetPicByBuf():
    img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
    fhand=open('cover2.jpg','wb')
    size=0
    while True:
        buf=img.read(100000)
        if len(buf)<1:
            break
        fhand.write(buf)
        size+=len(buf)
    print(size,' characters copied.')
    fhand.close()

#urllibGetPicByBuf()

import urllib.request,urllib.parse,urllib.error
import re
import ssl
def urllibParsingHtml():
    ctx = ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    url=input('Enter-')
    html=urllib.request.urlopen(url,context=ctx).read()
    links=re.findall(b'href="(http[s]?://.+?)"',html)
    for link in links:
        print(link.decode())

#urllibParsingHtml()


import urllib.request,urllib.parse,urllib.error
import ssl
from bs4 import BeautifulSoup

#使用urllib和BeautifulSoup解析html
def urllibParseHtmlByBS():

    #忽略SSL证书错误
    ctx=ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    #使用urllib获取html
    #使用BeautifulSoup解析html
    url=input('Enter- ')
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')

    #提取所有标签
    tags=soup('a')
    for tag in tags:
        print(tag.get('href',None))

#urllibParseHtmlByBS()

def urllibParseHtmlAllByBS():

    #忽略SSL证书错误
    ctx=ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    #使用urllib获取html
    #使用BeautifulSoup解析html
    url=input('Enter- ')
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')

    #提取所有地址标签
    tags=soup('a')
    for tag in tags:
        #打印标签的各部分
        print('TAG:',tag)
        print('URL:',tag.get('href',None))
        print('Contents:',tag.contents[0])
        print('Attrs:',tag.attrs)


urllibParseHtmlAllByBS()



