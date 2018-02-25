#!/home/meteoda69/.local/bin/python3
# -*- coding: utf-8 -*-
import datetime
import requests
from   bs4 import BeautifulSoup

r = requests.get(
    'http://www.gismeteo.lt/city/daily/4150/',
    headers={'user-agent': 'Mozilla/5.0'}
)

soup = BeautifulSoup(r.content, 'html.parser')
temp=(soup.find('div', {'id': 'weather'}).find_all('div')[4].find('dd').text);
state=(soup.find('div', {'id': 'weather'}).find('td').text);
wdir=(soup.find('div', {'id': 'weather'}).find_all('div')[5].find('dl',attrs={'class':'wicon'})['title'])
wind=(soup.find('div', {'id': 'weather'}).find_all('div')[5].find('dd').text)
print('<span style="font-size: 14pt;"><strong>Dienos orai Palangoje:</strong></span><br><br>')
print('<strong>'+temp, state, wdir, wind+"<br>")
pressure=(soup.find('div', {'id': 'weather'}).find_all('div')[6].find('dd').text)
print ("Slėgis: "+pressure+"<br>")
hum=(soup.find('div', {'id': 'weather'}).find_all('div')[7].text)
print (("Oro drėgmė: "+hum).replace("drėg.","")+"<br>")
water=(soup.find('div', {'id': 'weather'}).find_all('div')[8].find('dd').text)
print (("Vandens temperatūra: "+water).replace("vanduo","")+"</strong><br><br>")
print('<span style="font-size: 14pt;"><strong>Savaitės orai Palangoje:</strong></span><br><br>')
day1=datetime.datetime.today().weekday()
if day1 ==0:
    day1str="Pirmadienis"
elif day1==1:
    day1str="Antradienis"
elif day1==2:
    day1str="Trečiadienis"
elif day1==3:
    day1str="Ketvirtadienis"
elif day1==4:
    day1str="Penktadienis"
elif day1==5:
    day1str="Šeštadienis"
elif day1==6:
    day1str="Sekmadienis"
print ('<p style="text-align: justify;"><strong>(Šiandien): '+day1str+'</strong><br>')
print ('<strong><span style="font-size: 10pt;">')
array=("00.00","06.00","12.00","18.00")
for i in range(0,4):
    var=(soup.find_all('tr',class_='wrow')[i]['id'])
    state=(soup.find('tr',{'id': var}).find_all('td')[1].text)
    temp=(soup.find('tr',{'id': var}).find_all('td')[2].find_all('span')[0].text)
    press=(soup.find('tr',{'id': var}).find_all('td')[3].find_all('span')[0].text)
    wdir=(soup.find('tr',{'id': var}).find_all('td')[4].find('dt')['title'])
    wind=(soup.find('tr',{'id': var}).find_all('td')[4].find_all('span')[0].text)
    hum=(soup.find('tr',{'id': var}).find_all('td')[5].text)
    print(array[i],state.ljust(15)+", temperatūra: "+temp+", slėgis: "+press+"Hg"+", vėjas "+wdir, wind+"m/s"+", drėgnumas: "+hum+"%<br>")
print("</span></strong></p>")
day2=day1+1
if day2 ==7:
    day2str="Pirmadienis"
elif day2==1:
    day2str="Antradienis"
elif day2==2:
    day2str="Trečiadienis"
elif day2==3:
    day2str="Ketvirtadienis"
elif day2==4:
    day2str="Penktadienis"
elif day2==5:
    day2str="Šeštadienis"
elif day2==6:
    day2str="Sekmadienis"
print('<p style="text-align: justify;"><strong><span style="font-size: 12pt;">'+day2str+'<br>')
print('</span><span style="font-size: 10pt;">')
for i in range(4,8):
    var=(soup.find_all('tr',class_='wrow')[i]['id'])
    state=(soup.find('tr',{'id': var}).find_all('td')[1].text)
    temp=(soup.find('tr',{'id': var}).find_all('td')[2].find_all('span')[0].text)
    press=(soup.find('tr',{'id': var}).find_all('td')[3].find_all('span')[0].text)
    wdir=(soup.find('tr',{'id': var}).find_all('td')[4].find('dt')['title'])
    wind=(soup.find('tr',{'id': var}).find_all('td')[4].find_all('span')[0].text)
    hum=(soup.find('tr',{'id': var}).find_all('td')[5].text)
    print(array[i-4],state.ljust(15)+", temperatūra: "+temp+", slėgis: "+press+"Hg"+", vėjas "+wdir, wind+"m/s"+", drėgnumas: "+hum+"%<br>")
print("</span></strong></p>")
day3=day1+2
if day3 ==7:
    day3str="Pirmadienis"
elif day3==8:
    day3str="Antradienis"
elif day3==2:
    day3str="Trečiadienis"
elif day3==3:
    day3str="Ketvirtadienis"
elif day3==4:
    day3str="Penktadienis"
elif day3==5:
    day3str="Šeštadienis"
elif day3==6:
    day3str="Sekmadienis"
print("<strong>"+day3str+"</strong><br>")
print('<strong><span style="font-size: 10pt;">')
for i in range(8,12):
    var=(soup.find_all('tr',class_='wrow')[i]['id'])
    state=(soup.find('tr',{'id': var}).find_all('td')[1].text)
    temp=(soup.find('tr',{'id': var}).find_all('td')[2].find_all('span')[0].text)
    press=(soup.find('tr',{'id': var}).find_all('td')[3].find_all('span')[0].text)
    wdir=(soup.find('tr',{'id': var}).find_all('td')[4].find('dt')['title'])
    wind=(soup.find('tr',{'id': var}).find_all('td')[4].find_all('span')[0].text)
    hum=(soup.find('tr',{'id': var}).find_all('td')[5].text)
    print(array[i-8],state.ljust(15)+", temperatūra: "+temp+", slėgis: "+press+"Hg"+", vėjas "+wdir, wind+"m/s"+", drėgnumas: "+hum+"%<br>")
print("</span></strong><br>")
day4=day1+3
if day4 ==7:
    day4str="Pirmadienis"
elif day4==8:
    day4str="Antradienis"
elif day4==9:
    day4str="Trečiadienis"
elif day4==3:
    day4str="Ketvirtadienis"
elif day4==4:
    day4str="Penktadienis"
elif day4==5:
    day4str="Šeštadienis"
elif day4==6:
    day4str="Sekmadienis"
print("<strong>"+day4str+"</strong><br>")
print('<strong><span style="font-size: 10pt;">')
m = requests.get(
    'http://www.gismeteo.lt/city/daily/4150/2/',
    headers={'user-agent': 'Mozilla/5.0'}
    )
soup = BeautifulSoup(m.content, 'html.parser')
for i in range(4,8):
    var=(soup.find_all('tr',class_='wrow')[i]['id'])
    state=(soup.find('tr',{'id': var}).find_all('td')[1].text)
    temp=(soup.find('tr',{'id': var}).find_all('td')[2].find_all('span')[0].text)
    press=(soup.find('tr',{'id': var}).find_all('td')[3].find_all('span')[0].text)
    wdir=(soup.find('tr',{'id': var}).find_all('td')[4].find('dt')['title'])
    wind=(soup.find('tr',{'id': var}).find_all('td')[4].find_all('span')[0].text)
    hum=(soup.find('tr',{'id': var}).find_all('td')[5].text)
    print(array[i-4],state.ljust(15)+", temperatūra: "+temp+", slėgis: "+press+"Hg"+", vėjas "+wdir, wind+"m/s"+", drėgnumas: "+hum+"%<br>")
print("</span></strong><br>")
day5=day1+4
if day5 ==7:
    day5str="Pirmadienis"
elif day5==8:
    day5str="Antradienis"
elif day5==9:
    day5str="Trečiadienis"
elif day5==10:
    day5str="Ketvirtadienis"
elif day5==4:
    day5str="Penktadienis"
elif day5==5:
    day5str="Šeštadienis"
elif day5==6:
    day5str="Sekmadienis"
print("<strong>"+day5str+"</strong><br>")
print('<strong><span style="font-size: 10pt;">')
for i in range(8,12):
    var=(soup.find_all('tr',class_='wrow')[i]['id'])
    state=(soup.find('tr',{'id': var}).find_all('td')[1].text)
    temp=(soup.find('tr',{'id': var}).find_all('td')[2].find_all('span')[0].text)
    press=(soup.find('tr',{'id': var}).find_all('td')[3].find_all('span')[0].text)
    wdir=(soup.find('tr',{'id': var}).find_all('td')[4].find('dt')['title'])
    wind=(soup.find('tr',{'id': var}).find_all('td')[4].find_all('span')[0].text)
    hum=(soup.find('tr',{'id': var}).find_all('td')[5].text)
    print(array[i-8],state.ljust(15)+", temperatūra: "+temp+", slėgis: "+press+"Hg"+", vėjas "+wdir, wind+"m/s"+", drėgnumas: "+hum+"%<br>")
print("</span></strong><br>")
day6=day1+5
if day6 ==7:
    day6str="Pirmadienis"
elif day6==8:
    day6str="Antradienis"
elif day6==9:
    day6str="Trečiadienis"
elif day6==10:
    day6str="Ketvirtadienis"
elif day6==11:
    day6str="Penktadienis"
elif day6==5:
    day6str="Šeštadienis"
elif day6==6:
    day6str="Sekmadienis"
print("<strong>"+day6str+"</strong><br>")
print('<strong><span style="font-size: 10pt;">')
v = requests.get(
    'http://www.gismeteo.lt/city/daily/4150/4/',
    headers={'user-agent': 'Mozilla/5.0'}
)
soup = BeautifulSoup(v.content, 'html.parser')
for i in range(4,8):
    var=(soup.find_all('tr',class_='wrow')[i]['id'])
    state=(soup.find('tr',{'id': var}).find_all('td')[1].text)
    temp=(soup.find('tr',{'id': var}).find_all('td')[2].find_all('span')[0].text)
    press=(soup.find('tr',{'id': var}).find_all('td')[3].find_all('span')[0].text)
    wdir=(soup.find('tr',{'id': var}).find_all('td')[4].find('dt')['title'])
    wind=(soup.find('tr',{'id': var}).find_all('td')[4].find_all('span')[0].text)
    hum=(soup.find('tr',{'id': var}).find_all('td')[5].text)
    print(array[i-4],state.ljust(15)+", temperatūra: "+temp+", slėgis: "+press+"Hg"+", vėjas "+wdir, wind+"m/s"+", drėgnumas: "+hum+"%<br>")
print("</span></strong><br>")
day7=day1+6
if day7 ==7:
    day7str="Pirmadienis"
elif day7==8:
    day7str="Antradienis"
elif day7==9:
    day7str="Trečiadienis"
elif day7==10:
    day7str="Ketvirtadienis"
elif day7==11:
    day7str="Penktadienis"
elif day7==12:
    day7str="Šeštadienis"
elif day7==6:
    day7str="Sekmadienis"
print("<strong>"+day7str+"</strong><br>")
print('<strong><span style="font-size: 10pt;">')
for i in range(8,12):
    var=(soup.find_all('tr',class_='wrow')[i]['id'])
    state=(soup.find('tr',{'id': var}).find_all('td')[1].text)
    temp=(soup.find('tr',{'id': var}).find_all('td')[2].find_all('span')[0].text)
    press=(soup.find('tr',{'id': var}).find_all('td')[3].find_all('span')[0].text)
    wdir=(soup.find('tr',{'id': var}).find_all('td')[4].find('dt')['title'])
    wind=(soup.find('tr',{'id': var}).find_all('td')[4].find_all('span')[0].text)
    hum=(soup.find('tr',{'id': var}).find_all('td')[5].text)
    print(array[i-8],state.ljust(15)+", temperatūra: "+temp+", slėgis: "+press+"Hg"+", vėjas "+wdir, wind+"m/s"+", drėgnumas: "+hum+"%<br>")
print("</span></strong><br>")
print('<span style="font-size: 14pt;"><strong>Dviejų savaičių orai Palangoje:</strong></span><br><br>')
print("<strong>")
w = requests.get(
    'https://www.gismeteo.lt/city/weekly/4150/',
    headers={'user-agent': 'Mozilla/5.0'}
)
soup = BeautifulSoup(w.content, 'html.parser')
for i in range (0,13):
    day=(soup.find_all('div',class_='rframe wblock wdata')[i].find_all('td')[0].find_all('div')[0].text)
    dayname=(soup.find_all('div',class_='rframe wblock wdata')[i].find_all('td')[0].find_all('div')[1].text)
    mint=(soup.find_all('div',class_='rframe wblock wdata')[i].find_all('td')[3].find_all('span')[0].text)
    maxt=(soup.find_all('div',class_='rframe wblock wdata')[i].find_all('td')[6].find_all('span')[0].text)
    print(day,dayname,"Temperatūra nuo "+mint+" iki "+maxt+"<br>")
print("</strong>")
