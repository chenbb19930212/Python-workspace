from suds.client import Client

class ademoproject:
	def __init__(self,client):
		self.client=client

	def fjqz(self):
		arg0='<?xml version="1.0" encoding="UTF-8"?><root><nodeId>SFCK</nodeId><nodeName>司法查控系统</nodeName><caseId>DYH00000120191129000003</caseId><caseDate></caseDate><strSealname>123</strSealname><strSealPassword></strSealPassword><strKeyword>协助查询通知书</strKeyword><nPage>1</nPage><file><strFileName>协查通知书(福建银行).pdf</strFileName><strFileType>1</strFileType><strFileContent></strFileContent></file></root>'
		result=self.client.service.fjqz(arg0)
		print(result)


user_url='http://192.168.1.103:8083/demoService/webservice/FjqzConvertData?wsdl'
client=Client(user_url)
# print(client)
ad=ademoproject(client)
ad.fjqz()