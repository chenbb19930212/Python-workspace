from suds.client import Client
# from base64test import base64demo as b64
# from readfilexml import readfile
from rebuildxml import rebuildcode
# from SublimeTest.readfile import readfile as rd
class ckwipcloud:
	def __init__(self,client):
		self.client=client

	def feedBdcQL(self):
		bhdm=''
		#XZDWDM=IP000001
		# arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxVU0VSTUFSS0VSPjxDT05ESVRJT04+PFVTRVJOQU1FPlNWQXdNREF3TURFPTwvVVNFUk5BTUU+PFBBU1NXT1JEPk1USXo8L1BBU1NXT1JEPjwvQ09ORElUSU9OPjwvVVNFUk1BUktFUj4NCg=='
		# arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxVU0VSTUFSS0VSPjxDT05ESVRJT04+PFVTRVJOQU1FPlNWQXdNREF3TURRPTwvVVNFUk5BTUU+PFBBU1NXT1JEPk1USXo8L1BBU1NXT1JEPjwvQ09ORElUSU9OPjwvVVNFUk1BUktFUj4NCg=='
		argxml=r'<?xml version="1.0" encoding="UTF-8"?><USERMARKER><CONDITION><USERNAME>IP000004</USERNAME><PASSWORD>123</PASSWORD></CONDITION></USERMARKER>'
		arg0=rebuildcode(argxml,'UTF-8').rebuild()
		filename=r'E:\python-workspace\WebServiceInterface\ckw2016\testxml\ipcx.xml'
		arg1=rebuildcode(filename,'UTF-8').rebuild()
		# arg1='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxNZXNzYWdlPjxIZWFkPjxDUkVBVEVUSU1FPk1qQXhOaTh3Tmk4d015QXdPVG94TVRveU5BPT08L0NSRUFURVRJTUU+PFJFU1BPTlNFQ09ERT5NREF3TUE9PTwvUkVTUE9OU0VDT0RFPjxSRVNQT05TRUlORk8+PC9SRVNQT05TRUlORk8+PERJR0lUQUxTSUdOIG5hbWU9Inl2M1gxc2Vwdy9zPSI+PC9ESUdJVEFMU0lHTj48L0hlYWQ+PERhdGE+PEJEQ0ZLTElTVD48QkRDQ1hKRyBuYW1lPSJzcnUycjdMNnN1blJyNzNodWZzPSI+PENYUVFESD5RVEl3TVRreE1ESXhSVEF4TURBd01EQXdNREU9PC9DWFFRREg+PFJFU1VMVD5NREF3TUE9PTwvUkVTVUxUPjxESkJXSj48L0RKQldKPjxURFNZUUxJU1Q+PFREU1lRIG5hbWU9InpjRzEyTXY1MDlESXFBPT0iPjxCRENEWUg+TVRNd01UQXlNREV5TURJelNrRXdNREF3TVZjd01EQXdNREF3TUE9PTwvQkRDRFlIPjxaTD5RY3JRUThmNFJMVGw8L1pMPjxaRE1KPk9USTVORE11TmpZPTwvWkRNSj48TUpEVz5NZz09PC9NSkRXPjxZVD5NRGN4PC9ZVD48UUxYWj5NVEF3PC9RTFhaPjxCRENRWkg+eTlVb01qQXhPU2xCeXRDeXU3YXZzdnJJcUxYYU1EQXdNREF4dXNVPTwvQkRDUVpIPjxESkpHPnhNKytxY3JRc3J1MnI3TDZ0Y2U4eDd2NnViaz08L0RKSkc+PC9URFNZUT48L1REU1lRTElTVD48SlNZRFNZUUxJU1Q+PEpTWURTWVEgbmFtZT0idmFqSjZOUER0ZGpLdWRQRHlLaWhvdFdzdS9tMTJNcTUwOFBJcUE9PSI+PEJEQ0RZSD5NVE13TVRBeU1ERXpNREE0UjBJd01EQXdNbGN3TURBd01EQXdNQT09PC9CRENEWUg+PFpMPlFjclFRc2Y0ek9YVC9iR3h0UE85MWpFd3VzVT08L1pMPjxZVD5NRGcwPC9ZVD48U1lRTUo+TVRJMTwvU1lRTUo+PFFMWFo+TVRBeDwvUUxYWj48U1lRUVNTSj5NakF4T0M4d01TOHdNUT09PC9TWVFRU1NKPjxTWVFKU1NKPk1qQXhPREV5TVRJdk1UST08L1NZUUpTU0o+PEJEQ1FaSD55OVVvTWpBeE9TbEN5dEN5dTdhdnN2cklxTFhhTURBd01EQXl1c1U9PC9CRENRWkg+PERKSkc+enQ3Ty9iSzd0cSt5K3JYSHZNZTcrcm01PC9ESkpHPjwvSlNZRFNZUT48L0pTWURTWVFMSVNUPjxGRENRTElTVD48RkRDUSBuYW1lPSJ0NysxMkxMNnlLZz0iPjxCRENEWUg+TVRNd01UQTFNREEyTURBeFIwSXdNREF3TWtZd01EQXhNREF3TVE9PTwvQkRDRFlIPjxGRFpMPlFjclFRc2Y0UTlDaHgvaEZOaTB6TFRJd01nPT08L0ZEWkw+PEpaTUo+TlRBdU5qUT08L0paTUo+PFpZSlpNSj5OVEF1TURBPTwvWllKWk1KPjxGVEpaTUo+TVRBdU5qUT08L0ZUSlpNSj48R0hZVD5NVEU9PC9HSFlUPjxGV1haPk1BPT08L0ZXWFo+PEpHU0o+TWpBeE9DOHdNeTh5TUE9PTwvSkdTSj48VERTWVFTU0o+TWpBeE9DOHdOUzh5TUE9PTwvVERTWVFTU0o+PFREU1lKU1NKPk1qQXlNaTh3TlM4eU1BPT08L1REU1lKU1NKPjxCRENRWkg+eTlVb01qQXhPQ2xEeXRDeXU3YXZzdnJJcUxYYU1EQXdNREF6dXNVPTwvQkRDUVpIPjxESkpHPlE4clFzcnUycjdMNnRjZTh4OWJRME1RPTwvREpKRz48L0ZEQ1E+PC9GRENRTElTVD48SFlTWVFMSVNUPjxIWVNZUSBuYW1lPSJ1cVBUOGlpNnJNN2V2dFBEOGJxanRib3B5cm5UdzhpbyI+PEJEQ0RZSD5PVEV3TlRBME1UQTFNakF6UjBnd01EQXlORWd3TURBeE1EQXdNUT09PC9CRENEWUg+PFhNTUM+eExQVHc3cWp6KzdFdnc9PTwvWE1NQz48WUhXWlNNPnhMUEVzN3FqMC9JPTwvWUhXWlNNPjxZSExYQT5NZz09PC9ZSExYQT48WUhMWEI+TWpRPTwvWUhMWEI+PEhETUM+ek5LN3FMVzY8L0hETUM+PEhEV1o+MXRDNStzVFB1cVBYK0xIcVdGaFlXQT09PC9IRFdaPjxIRFlUPk1RPT08L0hEWVQ+PFNZUU1KPk9UQXdMakF3TURBPTwvU1lRTUo+PFNZUVFTU0o+TWpBeE9TOHdNUzh3TVE9PTwvU1lRUVNTSj48U1lRSlNTSj5NakF4T1M4eE1TOHhNUT09PC9TWVFKU1NKPjxCRENRWkg+eTlVb01qQXhPQ2xFeXRDeXU3YXZzdnJJcUxYYU1EQXdNREEwdXNVPTwvQkRDUVpIPjxESkpHPlJNclFzcnUycjdMNnRjZTh4OWJRME1RPTwvREpKRz48L0hZU1lRPjwvSFlTWVFMSVNUPjxHSlpXU1lRTElTVD48R0paV1NZUSBuYW1lPSJ1Ym1qcUwyb282blcvczd2eS9uVDBNaW8iPjxCRENEWUg+TlRFd05UQTBNVEExTWpBelIwSXdNREF5TkZRd01EQXhNREF3TVE9PTwvQkRDRFlIPjxaTD5zZlc2L3NmNDFNYTV5TUszMHRURXp3PT08L1pMPjxHSlpXR0hZVD55Y3pTdGRQRHpiND08L0dKWldHSFlUPjxHSlpXTUo+TVRBd0xqQXc8L0dKWldNSj48VERIWVNZUVNTSj5NakF4TVM4d05DOHhNZz09PC9UREhZU1lRU1NKPjxUREhZU1lKU1NKPk1qQXhPQzh3T1M4d09RPT08L1RESFlTWUpTU0o+PEJEQ1FaSD55OVVvTWpBeE9DbEZ5dEN5dTdhdnN2cklxTFhhTURBd01EQTF1c1U9PC9CRENRWkg+PERKSkc+UmNyUXNydTJyN0w2dGNlOHg5YlEwTVE9PC9ESkpHPjwvR0paV1NZUT48L0dKWldTWVFMSVNUPjxMUUxJU1Q+PExRIG5hbWU9IndkYklxQT09Ij48QkRDRFlIPk5URXdOVEEwTVRBMU1qQXpSMEl3TURBeU5GUXdNREF4TURBd01nPT08L0JEQ0RZSD48Wkw+eE0rK3FibkV3cVhIK0xuRXdxVzVxOVN3PC9aTD48U1lRTUo+TVRVd05qSXVNREF3TUE9PTwvU1lRTUo+PExEU1lRU1NKPk1qQXdNUzh3TlM4d01RPT08L0xEU1lRU1NKPjxMRFNZSlNTSj5NakF5TUM4eE1pOHhNZz09PC9MRFNZSlNTSj48TERTWVFYWj5NakF3PC9MRFNZUVhaPjxCRENRWkg+eTlVb01qQXhPQ2xHeXRDeXU3YXZzdnJJcUxYYU1EQXdNREEydXNVPTwvQkRDUVpIPjxESkpHPlJzclFzcnUycjdMNnRjZTh4OWJRME1RPTwvREpKRz48L0xRPjwvTFFMSVNUPjxEWUFRTElTVD48RFlBUSBuYW1lPSJ0ZGJSdXNpbyI+PEJEQ0RZSD5NVE13TVRBMU1EQTJNREF4UjBJd01EQXdNa1l3TURBeE1EQXdNUT09PC9CRENEWUg+PERZQkRDTFg+TWc9PTwvRFlCRENMWD48Wkw+UWNyUVFzZjRROUNoeC9oRk5pMHpMVEl3TWc9PTwvWkw+PERZUj56ZlcyL2c9PTwvRFlSPjxEWUZTPk1RPT08L0RZRlM+PERZUVI+MWNYSS9RPT08L0RZUVI+PERZUVJaSkxYPk9Uaz08L0RZUVJaSkxYPjxEWVFSWkpITT5NVEl6TkRVMk56ZzVNQT09PC9EWVFSWkpITT48RFlRUkxYRlM+TVRJek5EVTJOemc1TUE9PTwvRFlRUkxYRlM+PEJEQlpaUVNFPk1UQXdMakF3TURBPTwvQkRCWlpRU0U+PFpXTFhRU1NKPk1qQXhPUzh3TWk4eU5BPT08L1pXTFhRU1NKPjxaV0xYSlNTSj5NakF4T1M4eE1DOHdNUT09PC9aV0xYSlNTSj48QkRDREpaTUg+eTlVb01qQXhPQ2xIeXRDeXU3YXZzdnJJcUxYYU1EQXdNREEzdXNVPTwvQkRDREpaTUg+PERKSkc+UjhyUXNydTJyN0w2dGNlOHg5YlEwTVE9PC9ESkpHPjwvRFlBUT48L0RZQVFMSVNUPjxZR0RKTElTVD48WUdESiBuYW1lPSIxS1M0NXJYSHZNYz0iPjxCRENEWUg+TVRNd01UQTFNREEyTURBeFIwSXdNREF3TWtZd01EQXhNREF4TVE9PTwvQkRDRFlIPjxZR0RKWkw+TVE9PTwvWUdESlpMPjxaTD5RY3JRUXNmNFE5Q2h4L2hGTmkwekxUSXdNUT09PC9aTD48R0hZVD5Nek09PC9HSFlUPjxKWk1KPk1UQXdMakF3PC9KWk1KPjxCRENESlpNSD55OVVvTWpBeE9DbEl5dEN5dTdhdnN2cklxTFhhTURBd01EQTR1c1U9PC9CRENESlpNSD48REpKRz5TTXJRc3J1MnI3TDZ0Y2U4eDliUTBNUT08L0RKSkc+PC9ZR0RKPjwvWUdESkxJU1Q+PENGREpMSVNUPjxDRkRKIG5hbWU9InN1bTM0clhIdk1jPSI+PEJEQ0RZSD5NVE13TVRBMU1EQTJNREF4UjBJd01EQXdNa1l3TURBeE1EQXdNUT09PC9CRENEWUg+PFpMPlFjclFRc2Y0UTlDaHgvaEZOaTB6TFRJd01nPT08L1pMPjxDRkpHPlFjclExdEM4dHNqTHcvRzNxTlM2PC9DRkpHPjxDRkxYPk1RPT08L0NGTFg+PENGV0g+c3VtMzRzN0V1c1U9PC9DRldIPjxDRlFTU0o+TWpBeE5TOHdOeTh6TUE9PTwvQ0ZRU1NKPjxDRkpTU0o+TWpBeE5pOHdOQzh5TWc9PTwvQ0ZKU1NKPjxESkpHPlNzclFzcnUycjdMNnRjZTh4OWJRME1RPTwvREpKRz48L0NGREo+PC9DRkRKTElTVD48L0JEQ0NYSkc+PC9CRENGS0xJU1Q+PC9EYXRhPjwvTWVzc2FnZT4NCg=='
		
		# print(arg1)
		result=self.client.service.feedBdcQL(arg0,arg1)
		print(result)
	def cxwsInfo(self):
		argxml=r'<?xml version="1.0" encoding="UTF-8"?><USERMARKER><CONDITION><USERNAME>IP000002</USERNAME><PASSWORD>123</PASSWORD></CONDITION></USERMARKER>'
		arg0=rebuildcode(argxml,'UTF-8').rebuild()
		arg1xml=r'<?xml version="1.0" encoding="utf-8"?><xml><CONDITION><WSBH>AIP00000220200319000010</WSBH></CONDITION></xml>'
		arg1=rebuildcode(arg1xml,'UTF-8').rebuild()
		result=self.client.service.cxwsInfo(arg0,arg1)
		print(result)

	def kzBdcQL(self):
		argxml=r'<?xml version="1.0" encoding="UTF-8"?><USERMARKER><CONDITION><USERNAME>IP000002</USERNAME><PASSWORD>123</PASSWORD></CONDITION></USERMARKER>'
		arg0=rebuildcode(argxml,'UTF-8').rebuild()
		result=self.client.service.kzBdcQL(arg0)
		print(result)

	def feedkzBdcQL(self):
		# arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxVU0VSTUFSS0VSPjxDT05ESVRJT04+PFVTRVJOQU1FPlNWQXdNREF3TURFPTwvVVNFUk5BTUU+PFBBU1NXT1JEPk1USXo8L1BBU1NXT1JEPjwvQ09ORElUSU9OPjwvVVNFUk1BUktFUj4NCg=='
		argxml=r'<?xml version="1.0" encoding="UTF-8"?><USERMARKER><CONDITION><USERNAME>IP000004</USERNAME><PASSWORD>123</PASSWORD></CONDITION></USERMARKER>'
		arg0=rebuildcode(argxml,'UTF-8').rebuild()
		filename=r'E:\python-workspace\WebServiceInterface\ckw2016\testxml\ipkz.xml'
		arg1=rebuildcode(filename,'UTF-8').rebuild()
		# arg1='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxNZXNzYWdlPjxIZWFkPjxDUkVBVEVUSU1FPk1qQXhPQzh3Tmk4eU1pQXdPVG94TVRveU5BPT08L0NSRUFURVRJTUU+PFJFU1BPTlNFQ09ERT5NREF3TUE9PTwvUkVTUE9OU0VDT0RFPjxSRVNQT05TRUlORk8+PC9SRVNQT05TRUlORk8+PERJR0lUQUxTSUdOIG5hbWU9Inl2M1gxc2Vwdy9zPSI+PC9ESUdJVEFMU0lHTj48L0hlYWQ+PERhdGE+PEJEQ0ZLTElTVD48QkRDS1pKRyBuYW1lPSJzcnUycjdMNnY5ald4cjNodWZzPSI+PENYUVFESD5RVEl3TVRreE1ESXhSVEF5TURBd01EQXdNRE09PC9DWFFRREg+PFJFU1VMVD5NREF3TUE9PTwvUkVTVUxUPjxLWlhYTElTVD48S1pYWCBuYW1lPSJ2OWpXeHIzaHVmdlF4YytpIj48QkRDUUxMWD5NUT09PC9CRENRTExYPjxCRENEWUg+TVRNd01UQXlNREV5TURJelNrRXdNREF3TVZjd01EQXdNREF3TUE9PTwvQkRDRFlIPjxCRENRWkg+eTlVb01qQXhPU2xCeXRDeXU3YXZzdnJJcUxYYU1EQXdNREF4dXNVPTwvQkRDUVpIPjxLWlpUPk1RPT08L0taWlQ+PENTS1NSUT5NakF4T0Mwd05TMHdNUT09PC9DU0tTUlE+PENTSlNSUT5NakF4T0Mwd05pMHlNZz09PC9DU0pTUlE+PFdOS1pZWT56dDQ9PC9XTktaWVk+PEJFSVo+c2JqWG9qRXhNUT09PC9CRUlaPjwvS1pYWD48L0taWFhMSVNUPjwvQkRDS1pKRz48L0JEQ0ZLTElTVD48L0RhdGE+PC9NZXNzYWdlPg0K'
		# print(arg1)
		result=self.client.service.feedkzBdcQL(arg0,arg1)
		print(result)

user_url='http://192.168.1.103:8083/ckwipcloud/IpConvertData?wsdl'
client=Client(user_url)
print(client)
wb=ckwipcloud(client)

# wb.feedBdcQL() #查询反馈
# wb.cxwsInfo() #获取查询文书
# wb.kzBdcQL()  #控制请求
wb.feedkzBdcQL() #控制反馈