from suds.client import Client
import sys,os 
sys.path.append("..")
from rebuildxml import rebuildcode
from base64code import base64code

class xycjWebservice:
	def __init__(self,client):
		self.client=client

	def getSxbzxrList(self):
		param1=''
		param2=''
		

url=r'http://192.168.1.103:8082/xycjservice/SxbzxrConvertData?wsdl'
client=Client(url)
print(client)
# sxcj=sxcjWebservice(client)