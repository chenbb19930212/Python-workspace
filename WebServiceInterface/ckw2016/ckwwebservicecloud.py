from suds.client import Client
# from base64test import base64demo as b64
# from readfilexml import readfile
from rebuildxml import rebuildcode
# from SublimeTest.readfile import readfile as rd
class ckwwebservicecloud:
	def __init__(self,client):
		self.client=client

	def shfeedXzcxInfo(self):

		# arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjx1c2VybWFya2VyPjxjb25kaXRpb24gdXNlcm5hbWU9IldVZ3dNREF3TURFPSIgcGFzc3dvcmQ9Ik1USXoiPjwvY29uZGl0aW9uPjwvdXNlcm1hcmtlcj4='
		argold=r'<?xml version="1.0" encoding="UTF-8"?><usermarker><condition username="YH000001" password="123"></condition></usermarker>'
		arg0=rebuildcode(argold,'GBK').rebuild()
		print(arg0)
		filename=r'E:\python-workspace\WebServiceInterface\ckw2016\testxml\syyhcx.xml'
		# arg1=readfile(filename).read()
		arg1=rebuildcode(filename,'GBK').rebuild()
		# print(arg1)
		result=self.client.service.shfeedXzcxInfo(arg0,arg1)
		print(result)

	def shfeedXzkzInfo(self):
		# arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjx1c2VybWFya2VyPjxjb25kaXRpb24gdXNlcm5hbWU9IldVZ3dNREF3TURFPSIgcGFzc3dvcmQ9Ik1USXoiPjwvY29uZGl0aW9uPjwvdXNlcm1hcmtlcj4='
		argold=r'<?xml version="1.0" encoding="UTF-8"?><usermarker><condition username="YH000005" password="123"></condition></usermarker>'
		arg0=rebuildcode(argold,'GBK').rebuild()
		filename=r'E:\python-workspace\WebServiceInterface\ckw2016\testxml\syyhkz.xml'
		arg1=rebuildcode(filename,'GBK').rebuild()
		# print(arg1)
		result=self.client.service.shfeedXzkzInfo(arg0,arg1)
		print(result)

	def getXzcxList(self):
		arg0=r'	'

	def gjjfeedXzcxInfo(self):
		argold=r'<?xml version="1.0" encoding="utf-8"?><usermarker><condition username="JJ000004" password="123"/></usermarker>'
		arg0=rebuildcode(argold,'GBK').rebuild()
		filename=r'E:\python-workspace\WebServiceInterface\ckw2016\testxml\gjjcx.xml'
		arg1=rebuildcode(filename,'GBK').rebuild()
		result=self.client.service.gjjfeedXzcxInfo(arg0,arg1)
		print(result)


# user_url='http://192.168.1.103:8083/ckwWebServiceCloud/SyyhConvertData?wsdl'
user_url='http://192.168.1.103:8083/ckwWebServiceCloud/GjjConvertData?wsdl'
client=Client(user_url)
print(client)

wb=ckwwebservicecloud(client)
# YH行业
# wb.shfeedXzcxInfo()
# wb.shfeedXzkzInfo()
# Gjj行业
# wb.getXzcxList()
wb.gjjfeedXzcxInfo()