import base64
# b=base64.b64encode(b'我'.encoding=self.codetype)

class base64code():
	"""docstring for base64demo"""
	def __init__(self, arg,codetype):
		# super(base64demo, self).__init__()
		self.arg = arg
		if codetype !='':
			self.codetype = codetype
		else:
			self.codetype='utf-8'
		# print(type(self.arg))
		if(type(self.arg)==bytes):
			self.bytesString=self.arg
		if(type(self.arg)==str):
			self.bytesString = self.arg.encode(encoding=self.codetype)
		# self.arg2 = arg2 #readfile(arg2)
		# self.file1= readfile(arg)
		# self.file1 = readfile(arg2)
	
	def base64encode(self):
		# bytesString = self.arg.encode(encoding=self.codetype)
		b=base64.b64encode(self.bytesString)
		# print(b)
		return b.decode(encoding=self.codetype)

	def base64decode(self):
		# bytesString = self.arg.encode(encoding=self.codetype)
		b=base64.b64decode(self.bytesString)
		# print(b)
		return b.decode(encoding=self.codetype)

# bytesString = 'wo'.encode(encoding="utf-8")
# b=base64code(bytesString,'utf-8')
# result=b.base64encode()
# print(result)#b.decode(encoding="utf-8")