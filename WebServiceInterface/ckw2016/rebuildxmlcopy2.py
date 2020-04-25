from xml.dom.minidom import parse
from xml.dom.minidom import Document
import xml.dom.minidom
from base64code import base64code as b64

class rebuildcode(object):
  """docstring for ClassName"""
  def __init__(self, xmlpath):
    # super(ClassName, self).__init__()
    self.xmlpath = xmlpath

  def rebuild(self):
    # DOMTree = xml.dom.minidom.parse(r'C:\Users\Lenovo\Desktop\xml111.xml')

    DOMTree = xml.dom.minidom.parse(self.xmlpath)
    collection = DOMTree.documentElement
    print("主节点：",collection.nodeName)#主节点名
    list={}
    listattr={}

    #获取主节点的 下的 子节点
    for movie1 in collection.childNodes:
     print("子节点:",movie1)
     if movie1.nodeName =='#text':# and movie1.nodeValue !='\n    ' and movie1.nodeValue !='\n':
      if movie1.nodeValue.strip()!='':
       print("#text:",movie1.nodeValue.strip())
       
     if movie1.nodeName !='#text':
      #获取子节点的 子
      nndd=collection.getElementsByTagName(movie1.nodeName)[0].childNodes
      print(nndd)
      
      # tagvalue2=collection
      if nndd.length>0:
       node1 = collection.getElementsByTagName(movie1.nodeName)[0].childNodes[0]
       ttdd=movie1.attributes.values()
       attr={}
       for childtddd in ttdd:
    
        attr[childtddd.name]=childtddd.value
        listattr[movie1.nodeName]=attr
       print("listattr:",listattr) 
       list[movie1.nodeName]=node1.nodeValue
      elif nndd.length==0:
       list[movie1.nodeName]=''
      # print(collection.getElementsByTagName(nndd.length))
      # node1 = collection.getElementsByTagName(movie1.nodeName)[0].childNodes[0]
      # print(node1.nodeValue)
      # if node1.nodeValue!='':
      #  list[movie1.nodeName]=node1.nodeValue
      # else:
      #  list[movie1.nodeName]=''
      print("list:",list)
    doc=Document()
    root=doc.createElement(collection.nodeName)
    doc.appendChild(root)
    for node in list:
     # print(node)
     # print(list[node])
     newnodename=doc.createElement(node)
     text = doc.createTextNode(b64(list[node]).base64encode())# nodovalue base64加密
     print(type(text))#b64(list[node]).base64encode()
     newnodename.appendChild(text)
     ##添加attribute 属性和属性值
     print(node)
     if node in listattr:
        for attrs in listattr[node]:
          print(attrs)
          newnodename.setAttribute(attrs,b64(listattr[node][attrs]).base64encode())


     root.appendChild(newnodename)
     newxml=doc.toxml().replace('&quot;','\"')
    print(doc.toxml().replace('&quot;','\"'))
    
    
    # f = open('tel.xml','w',encoding = 'utf-8')
    # f.write(doc.toxml().replace('&quot;','\"'))
    # # f.write(doc.toprettyxml(indent = '\t', newl = '\n', encoding = 'utf-8'))
    # # doc.writexml(f,indent = '\t',newl = '\n', addindent = '\t',encoding = 'utf-8')
    # f.close()   
    return b64(newxml).base64encode()



path=r'E:\python-workspace\WebServiceInterface\ckw2016\testxml\ipkz.xml'
rb=rebuildcode(path)
rexml=rb.rebuild()
print(rexml)