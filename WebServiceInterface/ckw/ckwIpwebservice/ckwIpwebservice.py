from suds.client import Client
# from rebuildxml import rebuildcode
import sys,os
sys.path.append("..\\..")
from rebuildxml import rebuildcode

class ckwIpwebservice():
	def __init__(self,client):
		# pass
		self.client=client

	def cxBdcQL(self):
		argxml=r'<?xml version="1.0" encoding="UTF-8"?><USERMARKER><CONDITION><USERNAME>IP000008</USERNAME><PASSWORD>123</PASSWORD></CONDITION></USERMARKER>'
		arg0=rebuildcode(argxml,'utf-8').rebuild()
		result=self.client.service.cxBdcQL(arg0)
		print(result)


	def feedBdcQL(self):
		# arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxVU0VSTUFSS0VSPjxDT05ESVRJT04+PFVTRVJOQU1FPlNWQXdNREF3TURnPTwvVVNFUk5BTUU+PFBBU1NXT1JEPk1USXo8L1BBU1NXT1JEPjwvQ09ORElUSU9OPjwvVVNFUk1BUktFUj4NCg=='
		argxml=r'<?xml version="1.0" encoding="UTF-8"?><USERMARKER><CONDITION><USERNAME>IP000004</USERNAME><PASSWORD>123</PASSWORD></CONDITION></USERMARKER>'
		arg0=rebuildcode(argxml,'utf-8').rebuild()
		filename=sys.path[0]+r'\msgxml\ipcx.xml'
		arg1=rebuildcode(filename,'utf-8').rebuild()
		# print(arg1)
		result=self.client.service.feedBdcQL(arg0,arg1)
		print(result)

	def kzBdcQL(self):
		argxml=r'<?xml version="1.0" encoding="UTF-8"?><USERMARKER><CONDITION><USERNAME>IP000001</USERNAME><PASSWORD>123</PASSWORD></CONDITION></USERMARKER>'
		arg0=rebuildcode(argxml,'utf-8').rebuild()
		result=self.client.service.kzBdcQL(arg0)
		print(result)

	def feedkzBdcQL(self):
		# arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxVU0VSTUFSS0VSPjxDT05ESVRJT04+PFVTRVJOQU1FPlNWQXdNREF3TURnPTwvVVNFUk5BTUU+PFBBU1NXT1JEPk1USXo8L1BBU1NXT1JEPjwvQ09ORElUSU9OPjwvVVNFUk1BUktFUj4NCg=='	
		argxml=r'<?xml version="1.0" encoding="UTF-8"?><USERMARKER><CONDITION><USERNAME>IP000001</USERNAME><PASSWORD>123</PASSWORD></CONDITION></USERMARKER>'
		arg0=rebuildcode(argxml,'utf-8').rebuild()
		filename=sys.path[0]+r'\msgxml\ipkz.xml'
		arg1=rebuildcode(filename,'utf-8').rebuild()
		# print(arg1)
		result=self.client.service.feedkzBdcQL(arg0,arg1)
		print(result)

url=r'http://192.168.1.103:8083/ckwIpWebService/IpConvertDataAll?wsdl'
client=Client(url)
IP=ckwIpwebservice(client)
print(client)
# sys.path.append("..\\..")
# print(sys.path)
IP.cxBdcQL()
# IP.feedBdcQL()
# IP.kzBdcQL()
# IP.feedkzBdcQL()
