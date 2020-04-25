import base64
from readfilexml import readfile
# b=base64.b64encode(b'我'.encoding="utf-8")

class base64demo():
	"""docstring for base64demo"""
	def __init__(self, arg):
		# super(base64demo, self).__init__()
		self.arg = arg

		
		# self.arg = arg
		# self.arg2 = arg2 #readfile(arg2)
		# self.file1= readfile(arg)
		# self.file1 = readfile(arg2)
	#读取文档的方法
	def base64encode(self):
		text=readfile(self.arg).read()
		# print(text)
		bytesString = text.encode(encoding="utf-8")
		b=base64.b64encode(bytesString)
		return b.decode(encoding="utf-8")

#
	def base64decode(self):
		bytesString = self.arg.encode(encoding="utf-8")
		b=base64.b64decode(bytesString)
		# print(b)
		return b.decode(encoding="utf-8")
	#直接传str数据的解密方法
	def base64decodestr(self):
		bytesString = self.arg.encode(encoding="utf-8")
		
		b=base64.b64decode(bytesString)
		return b.decode(encoding="utf-8")

# param0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KDTxyZXNwb25zZT4KICA8Y29kZT5NUT09PC9jb2RlPgogIDxyZXNvdXJjZXVybD48L3Jlc291cmNldXJsPgogIDxtZXNzYWdlPjZLKzM1ckdDNTVxRTVyT1Y2Wm1pNUxpTjVhMlk1WnlvPC9tZXNzYWdlPgo8L3Jlc3BvbnNlPg=='
# base1=base64demo(param0)
# print(base1.base64decodestr())
# # param0='<?xml version="1.0" encoding="UTF-8"?><usermarker><condition username="WUgwMDAwMDM=" password="MTIz"></condition></usermarker>'
# param1='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjx1c2VybWFya2VyPjxjb25kaXRpb24gdXNlcm5hbWU9IldVZ3dNREF3TURFPSIgcGFzc3dvcmQ9Ik1USXoiPjwvY29uZGl0aW9uPjwvdXNlcm1hcmtlcj4NCg=='
# r=readfile(r'C:\Users\Administrator\Documents\SublimeText\zgyxml.txt')
# param0=r.read()

# base1=base64demo(param0,param1)
# print(base1.base64encode())


# f=r'C:\Users\Administrator\Documents\SublimeText\zgyxml.txt'
# base1=base64demo(f,param1)
# print(base1.base64encode())

# xml1=r'C:\Users\Administrator\Documents\SublimeText\ckwIpWebservice--IP.xml'
# base1=base64demo(xml1)
# print(base1.base64encode())

