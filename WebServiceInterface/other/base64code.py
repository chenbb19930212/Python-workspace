import base64
class base64coding():
	def __init__(self,code):
		self.code=code  ##编码格式 # GBK  UTF-8  UNICODE(非法)
		pass
	def b64encode(self,param):
		bytesString = param.encode(encoding=self.code)
		b=base64.b64encode(bytesString)
		# print(b)
		return b.decode(encoding=self.code)
		

	def b64decode(self,param):
		bytesString = param.encode(encoding=self.code)
		b=base64.b64decode(bytesString)
		# print(b)
		return b.decode(encoding=self.code)

p=base64coding('GBK')
p.b64encode('我')
