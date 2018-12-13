import mysql.connector,urllib.request, json, csv

nama_db = {
    'user':'root',
    'password':'lifeisgift',
    'host':'localhost',
    'database':'final_project'
}
koneksi=mysql.connector.connect(**nama_db)
kursor=koneksi.cursor()

'''
api_address = [
        'http://api.openweathermap.org/data/2.5/weather?q=Bekasi,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Jakarta,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Depok,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Bogor,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Tangerang,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Bandung,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Cirebon,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Banten,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Yogyakarta,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Kebumen,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Palembang,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Medan,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Aceh,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Padang,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Pekanbaru,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Denpasar,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Makassar,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Palu,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Banjarmasin,id&appid=2c79812cb5b96da223e2040a7ce36d45',
        'http://api.openweathermap.org/data/2.5/weather?q=Jayapura,id&appid=2c79812cb5b96da223e2040a7ce36d45'
        ]
reads = []
for url in api_address:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        reads.append(json.loads(html))
datalist=[]
for x in reads:
    #===ID_DETAIL===
    datalist.append([x.get('id', 'NULL'),x.get('name','NULL'),x.get('cod','NULL'),x.get('base','NULL'),x.get('visibility','NULL'),x.get('dt','NULL')])
    #===COORD===
    #datalist.append([x.get('id','NULL'),x['coord'].get('lon','NULL'),x['coord'].get('lat','NULL')])
    #===WEATHER===
    #datalist.append([x.get('id','NULL'),x['weather'][0].get('id','NULL')])
    #===MAIN===
    #datalist.append([x.get('id','NULL'),x['main'].get('temp','NULL'),x['main'].get('pressure','NULL'),x['main'].get('humidity','NULL'),x['main'].get('temp_min','NULL'),x['main'].get('temp_max','NULL')])
    #===WIND===
    #datalist.append([x.get('id', 'NULL'),x['wind'].get('speed','NULL'),x['wind'].get('deg','NULL')])
    #===CLOUD===
    #datalist.append([x.get('id', 'NULL'),x['clouds'].get('all','NULL')])
    #===SYS===
    #datalist.append([x.get('id', 'NULL'),x['sys'].get('type','NULL'),x['sys'].get('id','NULL'),x['sys'].get('message','NULL'),x['sys'].get('country','NULL'),x['sys'].get('sunrise','NULL'),x['sys'].get('sunset','NULL')])
      
with open('id_detail.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(datalist)
'''
#===MEMBUAT TABEL===

#kursor.execute('''
#CREATE TABLE id_detail(
#id INT PRIMARY KEY,
#name NVARCHAR(25),
#cod INT,
#base NVARCHAR(15),
#visibility INT,
#dt INT
#)''')

#kursor.execute('''
#CREATE TABLE weather_detail(
#weather_id INT,
#main_weather char(15),
#weather_desc char(50),
#weather_icon char(10))
#''')

#kursor.execute('''
#CREATE TABLE coord(
#id INT PRIMARY KEY,
#lon NVARCHAR(15),
#lat NVARCHAR(15))
#''')

#kursor.execute('''
#CREATE TABLE weather(
#id INT PRIMARY KEY,
#weather_id INT)
#''')

#kursor.execute('''
#CREATE TABLE main(
#id INT PRIMARY KEY,
#temp NVARCHAR(15),
#pressure NVARCHAR(15),
#humidity NVARCHAR(15),
#temp_min NVARCHAR(15),
#temp_max NVARCHAR(15))
#''')

#kursor.execute('''
#CREATE TABLE wind(
#id INT PRIMARY KEY,
#speed NVARCHAR(15),
#deg NVARCHAR(15))
#''')

#kursor.execute('''
#CREATE TABLE clouds(
#id INT PRIMARY KEY,
#cloud INT)
#''')

#kursor.execute('''
#CREATE TABLE sys(
#id INT PRIMARY KEY,
#type INT,
#sys_id INT,
#message NVARCHAR(15),
#country NVARCHAR(15),
#sunrise INT,
#sunset INT)
#''')

#koneksi.commit()

#===MENAMPILKAN DAFTAR TABEL===

#kursor.execute('SHOW TABLES')
#for (tabel,) in kursor:
#    print (tabel)

#===MENAMPILKAN TIPE DATA SEBUAH TABEL===

#kursor.execute('DESC weather_detail')
#for kolom in kursor:
#    print(kolom[0],kolom[1])

#===MEMASUKKAN DATA===
'''
kursor.execute("""INSERT INTO weather_detail VALUES
(200, 'thunderstorm', 'thunderstorm with light rain','11d'), 
(201, 'thunderstorm', 'thunderstorm with rain','11d'),
(202, 'thunderstorm', 'thunderstorm with heavy rain','11d'),
(210, 'thunderstorm', 'light thunderstorm','11d'),
(211, 'thunderstorm', 'thunderstorm','11d'),
(212, 'thunderstorm', 'heavy thunderstorm','11d'),
(221, 'thunderstorm', 'ragged thunderstorm','11d'),
(230, 'thunderstorm', 'thunderstorm with light drizzle','11d'),
(231, 'thunderstorm', 'thunderstorm with drizzle','11d'),
(232, 'thunderstorm', 'thunderstorm with heavy drizzle','11d'),
(300, 'drizzle', 'light intensity drizzle','09d'),
(301, 'drizzle', 'drizzle','09d'), 
(302, 'drizzle', 'heavy intensity drizzle','09d'),
(310, 'drizzle', 'light intensity drizzle rain','09d'),
(311, 'drizzle', 'drizzle rain','09d'),
(312, 'drizzle', 'heavy intensity drizzle rain','09d'),
(313, 'drizzle', 'shower rain and drizzle','09d'),
(314, 'drizzle', 'heavy shower rain and drizzle','09d'),
(321, 'drizzle', 'shower drizzle','09d'),
(500, 'rain', 'light rain','10d'),
(501, 'rain', 'moderate rain','10d'),
(502, 'rain', 'heavy intensity rain','10d'),
(503, 'rain', 'very heavy rain','10d'),
(504, 'rain', 'extreme rain','10d'),
(511, 'rain', 'freezing rain','13d'),
(520, 'rain', 'light instensity shower rain','09d'),
(521, 'rain', 'shower rain','09d'),
(522, 'rain', 'heavy intensity shower rain','09d'),
(531, 'rain', 'ragged shower rain','09d'),
(600, 'snow', 'light snow','13d'),
(601, 'snow', 'snow','13d'),
(602, 'snow', 'heavy snow','13d'),
(611, 'snow', 'sleet','13d'),
(612, 'snow', 'shower sleet','13d'),
(615, 'snow', 'light rain and snow','13d'),
(616, 'snow', 'rain and snow','13d'),
(620, 'snow', 'light shower snow','13d'),
(621, 'snow', 'shower snow','13d'),
(622, 'snow', 'heavy shower snow','13d'),
(701, 'atmosphere', 'mist','50d'),
(711, 'atmosphere', 'smoke','50d'),
(721, 'atmosphere', 'haze','50d'),
(731, 'atmosphere', 'sand, dust whirls','50d'),
(741, 'atmosphere', 'fog','50d'),
(751, 'atmosphere', 'sand','50d'),
(761, 'atmosphere', 'dust','50d'),
(762, 'atmosphere', 'volcanic ash','50d'),
(771, 'atmosphere', 'squalls','50d'),
(781, 'atmosphere', 'tornado','50d'),
(800, 'clear', 'clear sky', '01d'),
(801, 'clouds', 'few clouds', '02d'),
(802, 'clouds', 'scattered clouds', '03d'),
(803, 'clouds', 'broken clouds', '04d'),
(804, 'clouds', 'overcast clouds', '04d')
""")
koneksi.commit()
'''

#===IMPORT FILE CSV KE SQL===
#kursor.execute('''
#LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/id_detail.csv'
#INTO TABLE id_detail
#FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
#''')
#koneksi.commit()

koneksi.close()

