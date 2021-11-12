'''
1.Extracting Data from XML
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

def reqXmlCount():

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter url: ')
        if len(address) < 1: break

        #parms = dict()
        print('Retrieving', address)
        uh = urllib.request.urlopen(address, context=ctx)
        print(type(uh))

        data = uh.read()
        print(type(data))
        print('Retrieved', len(data), 'characters')
        #print(data.decode())
        tree = ET.fromstring(data)
        print(type(tree))

        results = tree.findall('comments/comment')
        counts=0
        for index in range(len(results)):
            countstr=results[index].find('count').text
            counts+=int(countstr)
        print('counts:',counts)

        res=tree.findall('.//count')
        print('res:',len(res))

#reqXmlCount()


import urllib.request, urllib.parse, urllib.error
import json
import ssl

def reqJsonCount():

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter url: ')
        if len(address) < 1: break

        #parms = dict()
        print('Retrieving', address)
        uh = urllib.request.urlopen(address, context=ctx)
        print(type(uh))

        data = uh.read()
        print(type(data))
        print('Retrieved', len(data), 'characters')
        #print(data.decode())
        info = json.loads(data)
        print(type(info))

        num=len(info['comments'])
        counts=0
        for index in range(num):
            count=info['comments'][index]['count']
            counts+=count

        print(counts)


#reqJsonCount()


import urllib.request, urllib.parse, urllib.error
import json
import ssl
def reqGoogleGeoJson():
    #1.设置请求url和key
    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    #2.设置忽略证书错误
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        #3.获取和组装请求链接
        address = input('Enter location: ')
        if len(address) < 1: break

        parms = dict()
        parms['address'] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        #4.调用urllib请求链接，接收、解码数据
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        #5.加载、解析json数据
        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        print(json.dumps(js, indent=4))

        place_id=js['results'][0]['place_id']
        print(place_id)

reqGoogleGeoJson()