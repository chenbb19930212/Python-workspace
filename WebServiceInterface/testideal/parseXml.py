import os
from xml.dom.minidom import parse
from xml.dom.minidom import Document
import xml.dom.minidom
from base64code import base64code as b64
class parsexml(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		# super(ClassName, self).__init__()
		self.arg = arg
	
	def readfile(self):
		
		with open(self.arg,'r',encoding='utf-8') as file_object:
			content=file_object.read()
			nr=content.rstrip()
		return nr

	def decodexml(self):
		try:
			DOMTree=parse(self.arg)
		except Exception as e:
			DOMTree=xml.dom.minidom.parseString(self.arg)
			# raise e
		

		collection = DOMTree.documentElement
		print(collection)
		return collection

	def loopxml(self):
		

filepath=r'E:\python-workspace\WebServiceInterface\testideal\testxml.txt'
p=parsexml(filepath)
cc=p.readfile()
# print(cc)

aa=b64(cc,'utf-8').base64decode()
print(aa)

PX=parsexml(aa)
# DOMTree=xml.dom.minidom.parseString(aa)
nr=PX.decodexml()
# collection = DOMTree.documentElement
print(nr.nodeName)

