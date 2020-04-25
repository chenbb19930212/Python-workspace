from suds.client import Client
import sys,os 
sys.path.append("..")
from rebuildxml import rebuildcode
from base64code import base64code
class sxcjWebservice:
	def __init__(self,client):
		self.client=client

	def getSxbzxrList(self):
		param1=base64code('YH000020','UTF-8').base64encode()
		param2=base64code('123','UTF-8').base64encode()
		xml=r'<?xml version="1.0" encoding="UTF-8"?><request><gxsja>2019/01/01 00:00:00</gxsja><gxsjb>2019/12/30 23:59:59</gxsjb><pagerows>15</pagerows><currentpage>1</currentpage><sjbs>1</sjbs></request>'
		# print(xml)
		param3=rebuildcode(xml,'GBK').rebuild()
		# print(param3)
		result=self.client.service.getSxbzxrList(param1,param2,param3)
		print(result)
	def getQgSxbzxrList(self):
		param1=base64code('YH000020','UTF-8').base64encode()
		param2=base64code('123','UTF-8').base64encode()
		xml=r'<?xml version="1.0" encoding="UTF-8"?><request><gxsja>2019/01/01 00:00:00</gxsja><gxsjb>2019/12/30 23:59:59</gxsjb><pagerows>15</pagerows><currentpage>1</currentpage><sjbs>2</sjbs></request>'
		# print(xml)
		param3=rebuildcode(xml,'GBK').rebuild()
		# print(param3)
		result=self.client.service.getQgSxbzxrList(param1,param2,param3)
		print(result)

	def getXzgxfList(self):
		param1=base64code('YH000020','UTF-8').base64encode()
		param2=base64code('123','UTF-8').base64encode()
		xml=r'<?xml version="1.0" encoding="UTF-8"?><request><gxsja>2019/01/01 00:00:00</gxsja><gxsjb>2019/12/30 23:59:59</gxsjb><pagerows>15</pagerows><currentpage>1</currentpage><sjbs>2</sjbs></request>'
		# print(xml)
		param3=rebuildcode(xml,'GBK').rebuild()
		# print(param3)
		result=self.client.service.getXzgxfList(param1,param2,param3)
		print(result)

	def getBzxrgkList(self):
		param1=base64code('YH000020','UTF-8').base64encode()
		param2=base64code('123','UTF-8').base64encode()

	def getSfgkList(self):
		param1=base64code('YH000020','UTF-8').base64encode()
		param2=base64code('123','UTF-8').base64encode()


url=r'http://192.168.1.103:8084/sxcjWebservice/SxConvertData?wsdl'
client=Client(url)
print(client)
sxcj=sxcjWebservice(client)
sxcj.getSxbzxrList()
# sxcj.getQgSxbzxrList()
# sxcj.getXzgxfList()