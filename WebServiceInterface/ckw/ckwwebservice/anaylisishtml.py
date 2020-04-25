
from bs4 import BeautifulSoup 
import requests
import re
url='http://192.168.1.115:8081/ckwWebService'
response=requests.get(url)
d=BeautifulSoup(response.text,'html.parser')
# print(d.find_all('span',class_='value'))
# print(d.find_all('a'))
v={}
for x in d.find_all('a'):
	# print(x['href'])
	# print(x.get_text())
	e=re.split('}*',x.get_text())
	url=x['href']
	# print(e[1])
	v[e[1][2]]=url

print(v)