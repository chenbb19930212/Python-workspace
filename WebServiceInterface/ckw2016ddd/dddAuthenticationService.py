from suds.client import Client
# from readfilexml import readfile
from base64test import base64demo as b64
class dddAuthenticationService:
	def __init__(self,client):
		self.client=client

	def getResourceByToken(self):
		# filename=r'C:\Users\Lenovo\Desktop\xml111.xml'
		# arg0=readfile(filename).read()
		# print(arg0)
		arg0=b64(r'E:\python-workspace\WebServiceInterface\ckw2016ddd\xml123.xml').base64encode()
		# print(arg0)
		result=self.client.service.getResourceByToken(arg0)
		print(result)

user_url='http://192.168.137.101:8081/ckwddd/service/dddAuthenticationService.ws?wsdl'
client=Client(user_url)
# print(client)
cx=dddAuthenticationService(client)
cx.getResourceByToken()