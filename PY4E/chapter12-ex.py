'''
Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
 You can use split('/') to break the URL into its component parts so you can extract the host name for the 
 socket connect call. Add error checking using try and except to handle the condition where the user enters 
 an improperly formatted or non-existent URL.
'''

#发送get请求获取文本文件
import socket
import time
def SendReqGetText():
    try:
        url=input('please enter a url(for read the html file): ')
        addr=url.split('/')
        addr=addr[2]
        print(addr)
        mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mysock.connect((addr, 80))
        cmd=('GET '+url+' HTTP/1.0\r\n\r\n')
        print(cmd)
        cmd=cmd.encode()
        print(cmd)

        mysock.send(cmd)
    except:
        print("wrong url:",url)
        exit()

    while True:
        data=mysock.recv(512)
        if len(data)<1:
            break
        print(data.decode(),end=' ')
    mysock.close()


#SendReqGetText()


#http://data.pr4e.org/romeo.txt

'''
Exercise 2: Change your socket program so that it counts the number of characters it has received and stops 
displaying any text after it has shown 3000 characters. The program should retrieve the entire document and 
count the total number of characters and display the count of the number of characters at the end of the 
document.
'''
def SendReqGetTextAndCount():
    try:
        url=input('please enter a url(for read the html file): ')
        addr=url.split('/')
        addr=addr[2]
        print(addr)
        mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mysock.connect((addr, 80))
        cmd=('GET '+url+' HTTP/1.0\r\n\r\n')
        print(cmd)
        cmd=cmd.encode()
        print(cmd)

        mysock.send(cmd)
    except:
        print('wrong url: ',url)
        exit()
    count=0
    display=''
    while True:
        data=mysock.recv(512)
        count+=len(data)
        display+=data.decode()
        if len(data)<1:
            break
    print(display[0:3000])
    print('total count:',count)
    mysock.close()

#SendReqGetTextAndCount()


'''
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
(2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
'''
import urllib.request
def urllibGetTextAndCount():
    try:
        url=input('Please enter a url: ')
        text=urllib.request.urlopen(url)
    except:
        print('wrong url: ',url)
        exit()
    count=0
    display=''
    for line in text:
        line=line.decode()
        line=line.rstrip()
        count+=len(line)
        display+=line
    print(display[0:3000])
    print('total count:',count)

#urllibGetTextAndCount()


'''
Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML 
document and display the count of the paragraphs as the output of your program. Do not display the paragraph 
text, only count them. Test your program on several small web pages as well as some larger web pages.
'''
#使用urllib和BeautifulSoup解析html
import urllib.request
from bs4 import BeautifulSoup
import ssl

def urllibParseHtmlByBSAndCountP():

    #忽略SSL证书错误
    ctx=ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    #使用urllib获取html
    #使用BeautifulSoup解析html
    url=input('Enter- ')
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')

    #统计所有的p标签
    count=0
    tags=soup('p')
    for tag in tags:
       count+=1
    print('Total paragraph tags: ',count)

#urllibParseHtmlByBSAndCountP()
'''
Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank 
line have been received. Remember that recv receives characters (newlines and all), not lines.

'''

#发送get请求获取文本文件
import socket
import time
def SendReqGetTextAndExtract():
    try:
        url=input('please enter a url(for read the html file): ')
        addr=url.split('/')
        addr=addr[2]
        #print(addr)
        mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mysock.connect((addr, 80))
        cmd=('GET '+url+' HTTP/1.0\r\n\r\n')
        #print(cmd)
        cmd=cmd.encode()
        #print(cmd)

        mysock.send(cmd)
    except:
        print("wrong url:",url)
        exit()
    display=''
    while True:
        data=mysock.recv(512)
        if len(data)<1:
            break
        display += data.decode()
    display=display[display.find('\r\n\r\n'):]
    print(display)
    mysock.close()

#SendReqGetTextAndExtract()    


import urllib.request
from bs4 import BeautifulSoup
import ssl

def urllibParseHtmlByBSAndCountSpanSum():

    #忽略SSL证书错误
    ctx=ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    #使用urllib获取html
    #使用BeautifulSoup解析html
    url=input('Enter- ')
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')

    #统计所有的p标签
    counts=0
    tags=soup('span')
    for tag in tags:
        counts+=int(str(tag.contents[0]))
        
    print('Total: ',counts)


#urllibParseHtmlByBSAndCountSpanSum()


def urllibParseHtmlByBS_ex3():

    #忽略SSL证书错误
    ctx=ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    #使用urllib获取html
    #使用BeautifulSoup解析html
    url=input('Enter url - ')
    position=int(input('Enter position - '))
    count=int(input('Enter count - '))
    print('position: ',position)
    print('count: ',count)

    t=0
    for index in range(count):  #循环count次
        print('index: ',index)
        print('url: ',url)
        t+=1
        html=urllib.request.urlopen(url,context=ctx).read()
        soup=BeautifulSoup(html,'html.parser')
        tags=soup('a')
        pos=1
        aim=''
        for tag in tags:        #循环position次
            if pos==position:
                if(t==count):
                    aim=tag.contents[0]
                    #print(tag)
                else:
                    url=tag.get('href',None)
                    break
            pos+=1
                
        
        
    print(aim)

urllibParseHtmlByBS_ex3()












