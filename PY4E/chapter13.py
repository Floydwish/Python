import xml.etree.ElementTree as ET

def parseXml():
    data = '''
    <person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes" />
    </person>'''

    tree=ET.fromstring(data)
    name=tree.find('name').text
    attr=tree.find('email').get('hide')

    print('name:',name)
    print('attr:',attr)

#parseXml()

import xml.etree.ElementTree as ET
def loopNodes():
    input = '''
    <stuff>
     <users>
      <user x="2">
       <id>001</id>
       <name>Chuck</name>
      </user>
      <user x="7">
       <id>009</id>
       <name>Brent</name>
      </user>
     </users>
    </stuff>'''

    stuff=ET.fromstring(input)
    lst=stuff.findall('users/user')
    print('Count: ',len(lst))
    for user in lst:
        print('name:',user.find('name').text)
        print('id:',user.find('id').text)
        print('attr:',user.get('x'))

#loopNodes()

import json

data = '''
[
    {"id" : "001",
     "x" : "2",
     "name" : "Chuck"
    } ,
    {"id" : "009",
     "x" : "7",
     "name" : "Brent"
    }
]'''

def parseJson():
    info=json.loads(data)
    print('count:',len(info))

    for item in info:
        print('id:',item['id'])
        print('name:',item['name'])
        print('attr:',item['x'])

#parseJson()


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

        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        print('lat', lat, 'lng', lng)
        location = js['results'][0]['formatted_address']
        print(location)


#reqGoogleGeoJson()


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

def reqGoogleGeoXml():
    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        parms = dict()
        parms['address'] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)

        data = uh.read()
        print('Retrieved', len(data), 'characters')
        print(data.decode())
        tree = ET.fromstring(data)

        results = tree.findall('result')
        lat = results[0].find('geometry').find('location').find('lat').text
        lng = results[0].find('geometry').find('location').find('lng').text
        location = results[0].find('formatted_address').text

        print('lat', lat, 'lng', lng)
        print(location)

#reqGoogleGeoXml()

'''
Exercise 1: Change either geojson.py (https://www.py4e.com/code3/geojson.py) or geoxml.py
(https://www.py4e.com/code3/geoxml.py) to print out the two-character country code from the
retrieved data. Add error checking so your program does not traceback if the country code is not
there. Once you have it working, search for “Atlantic Ocean” and make sure it can handle locations
that are not in any country
'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl

def reqGoogleGeoJsonParseCountry():
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

        #print(json.dumps(js, indent=4))

        #lat = js['results'][0]['geometry']['location']['lat']
        #lng = js['results'][0]['geometry']['location']['lng']
        #print('lat', lat, 'lng', lng)

        try:
            location = js['results'][0]['formatted_address']
            print(location)


            #print(type(js))
            addr=js['results'][0]['address_components']
            #print('len:',len(addr))
            country=addr[len(addr)-1]['types'][0]
            #print(country)
            if addr[len(addr)-1]['types'][0] == 'country':
                coun=addr[len(addr)-1]['short_name']
                print(coun)
        except:
            print('parse json error, please try agin!')
            continue



reqGoogleGeoJsonParseCountry()



'''
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Shenzhen",
                    "short_name": "Shenzhen",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Guangdong Province",
                    "short_name": "Guangdong Province",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "China",
                    "short_name": "CN",
                    "types": [
                        "country",
                        "political"
                    ]
                }
            ],
            "formatted_address": "Shenzhen, Guangdong Province, China",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 22.8617483,
                        "lng": 114.6284666
                    },
                    "southwest": {
                        "lat": 22.3963441,
                        "lng": 113.7514535
                    }
                },
                "location": {
                    "lat": 22.543096,
                    "lng": 114.057865
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 22.7809313,
                        "lng": 114.3553162
                    },
                    "southwest": {
                        "lat": 22.3293893,
                        "lng": 113.7524414
                    }
                }
            },
            "place_id": "ChIJkVLh0Aj0AzQRyYCStw1V7v0",
            "types": [
                "locality",
                "political"
            ]
        }
    ],
    "status": "OK"
}
'''

