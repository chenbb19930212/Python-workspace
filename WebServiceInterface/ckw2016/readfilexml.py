import chardet
class readfile(object):
	"""docstring for readfile"""
	def __init__(self, filename):
		# super(readfile, self).__init__()
		self.filename = filename

	def read(self):

		with open(self.filename,'r',encoding = "utf-8") as file_object:
			content=file_object.read()
			nr=content.rstrip()
			# print(nr)
			return nr

# r=readfile(r'C:\Users\Administrator\Documents\SublimeText\WebServiceInterface\ckw2016\testxml\syyhcx.xml')
# print(r.read())
