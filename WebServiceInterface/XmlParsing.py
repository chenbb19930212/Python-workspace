# from xml.etree import ElementTree as ET 
import xml.etree.ElementTree as ET
from base64code import base64coding as b64

# xml1='<?xml version="1.0" encoding="UTF-8"?><kzxxList><a1>123</a1><a2>456</a2></kzxxList>'
# tree = ET.ElementTree(xml1)
class xmlhandle(object):
	"""docstring for xmlhandle"""
	def __init__(self, arg):
		# super(xmlhandle, self).__init__()
		# self.arg = arg
		pass
	def forallchild(self,child):
		for childson in child:
			print(childson.tag,childson,attrib,childson.text)
	def xmlparse(self,xml):
		sb={}
		root=ET.XML(xml)
		for child in root:
			print(child.tag,child,attrib,child.text)
			forallchild(child)
	

	# def getallchild(self):

# xml1='<?xml version="1.0" encoding="utf-8"?><root><person age="18"><name>hzj</name><sex>man</sex></person><person age="19" des="hello"><name>kiki</name><sex>female</sex></person></root>'
# root =ET.fromstring(xml1)
# tree=ET.XML(xml1)
# print ("tree type:", type(tree),tree.tag)
# doc = ET.ElementTree(tree)
# # tree = ET.parse(xml1)
# print ("doc type:", type(doc))
# root=doc.getroot()
# print ("root type:", type(root))   

############string 类型
# xml1='<?xml version="1.0" encoding="utf-8"?><root><person age="18"><name>hzj</name><sex>man</sex></person><person age="19" des="hello"><name>kiki</name><sex>female</sex></person></root>'
# root=ET.XML(xml1)
# # print(root.getallchild())
# for child in root:
# 	print(child.tag,child.attrib,child.text)
# 	for nextchild in child:
# 		print(nextchild.tag,nextchild.attrib,nextchild.text)

# root.find
# print (tree.tag, "----", tree.attrib) 
#.getiterator("person")
# print(root)
# print(lst_node)
# for node in lst_node:
# 	print(node.text,node.attrib)
    # print_node(node)