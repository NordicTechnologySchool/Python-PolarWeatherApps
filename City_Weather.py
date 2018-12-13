import urllib.request #, json

def get_api_address(cities=None):
    if cities==None:
        cities=(
            'bekasi','jakarta','depok','bogor','tangerang','bandung','cirebon','banten','yogyakarta','kebumen','palembang','medan','aceh','padang','pekanbaru','denpasar','makassar','palu','banjarmasin','jayapura'
        )
    else:
        cities==cities
    api_address={
        'bekasi'     :'http://api.openweathermap.org/data/2.5/weather?q=Bekasi,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'jakarta'    :'http://api.openweathermap.org/data/2.5/weather?q=Jakarta,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'depok'      :'http://api.openweathermap.org/data/2.5/weather?q=Depok,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'bogor'      :'http://api.openweathermap.org/data/2.5/weather?q=Bogor,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'tangerang'  :'http://api.openweathermap.org/data/2.5/weather?q=Tangerang,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'bandung'    :'http://api.openweathermap.org/data/2.5/weather?q=Bandung,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'cirebon'    :'http://api.openweathermap.org/data/2.5/weather?q=Cirebon,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'banten'     :'http://api.openweathermap.org/data/2.5/weather?q=Banten,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'yogyakarta' :'http://api.openweathermap.org/data/2.5/weather?q=Yogyakarta,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'kebumen'    :'http://api.openweathermap.org/data/2.5/weather?q=Kebumen,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'palembang'  :'http://api.openweathermap.org/data/2.5/weather?q=Palembang,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'medan'      :'http://api.openweathermap.org/data/2.5/weather?q=Medan,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'aceh'       :'http://api.openweathermap.org/data/2.5/weather?q=Aceh,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'padang'     :'http://api.openweathermap.org/data/2.5/weather?q=Padang,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'pekanbaru'  :'http://api.openweathermap.org/data/2.5/weather?q=Pekanbaru,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'denpasar'   :'http://api.openweathermap.org/data/2.5/weather?q=Denpasar,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'makassar'   :'http://api.openweathermap.org/data/2.5/weather?q=Makassar,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'palu'       :'http://api.openweathermap.org/data/2.5/weather?q=Palu,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'banjarmasin':'http://api.openweathermap.org/data/2.5/weather?q=Banjarmasin,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'jayapura'   :'http://api.openweathermap.org/data/2.5/weather?q=Jayapura,id&appid=2c79812cb5b96da223e2040a7ce36d45'
        }
    get_address=[]
    for city in cities:
        city=city.lower()
        get_address.append(api_address[city])
    return get_address

#print(get_api_address(['bekasi','jakarta','depok','bogor','tangerang','bandung','cirebon','banten','yogyakarta','kebumen','palembang','medan','aceh','padang','pekanbaru','denpasar','makassar','palu','banjarmasin','jayapura']))

def get_city_based_on_name_value(cities=None):
    city_weather_list = []
    if cities==None:
        for url in get_api_address():
            with urllib.request.urlopen(url) as response:
                html = response.read()
                city_weather_list.append(html)
                #read = (json.loads(html))
                #INDONESIA_20.append(read)
        #return(html)
        return (city_weather_list)

    else:
        for url in get_api_address(cities):
            with urllib.request.urlopen(url) as response:
                html = response.read()
                city_weather_list.append(html)
        return (city_weather_list)

#for object in get_city_based_on_name_value():
#    print (object)
#    print('===')
#print (get_city_based_on_name_value(['bekasi','jakarta']))  # USE [] OR () INSIDE PARANTHESES TO PRINT DATA OF SPECIFIC CITY