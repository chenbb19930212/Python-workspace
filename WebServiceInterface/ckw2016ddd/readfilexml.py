import chardet
class readfile(object):
	"""docstring for readfile"""
	def __init__(self, filename):
		# super(readfile, self).__init__()
		
		self.filename = filename

	def read(self):
		print(self.filename)
		with open(self.filename,'r',encoding = "utf-8") as file_object:
			content=file_object.read()
			nr=content.rstrip()
			# print(nr)
			return nr

# filepath=r'C:\\Users\\Lenovo\\Desktop\\xml111.xml'
# readtest=readfile(r'C:\\Users\\Lenovo\\Desktop\\xml111.xml')
# print(readtest.read())	

