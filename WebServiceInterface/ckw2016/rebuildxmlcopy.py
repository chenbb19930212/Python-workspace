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
    ##解析xml
    DOMTree = xml.dom.minidom.parse(self.xmlpath)
    collection = DOMTree.documentElement
    # print("主节点：",collection.nodeName)#主节点名
    ##创建xml
    newdoc=Document()
    newroot=newdoc.createElement(collection.nodeName)
    newdoc.appendChild(newroot)
    #循环解析xml并同步创建新xml并base64加密
    self.loopxml(collection,newdoc,newroot)

  def loopxml(self,collection,newdoc,newroot):
    self.node=collection
    self.newdoc=newdoc
    self.newroot=newroot
    #获取主节点的 下的 子节点
    # print(self.node)
    # newnode=self.newdoc.createElement(node.nodeName)
    # self.newroot.appendChild(newnode)
    for childnodes in self.node.childNodes:
      if childnodes.nodeName =='#text':# and movie1.nodeValue !='\n    ' and movie1.nodeValue !='\n':
        value=childnodes.nodeValue
        text = self.newdoc.createTextNode(value) #b64(value).base64encode()
        newroot.appendChild(text)
        # if childnodes.nodeValue.strip()!='':
          # pass
          # print("#text:",childnodes.nodeValue.strip())
       
      if childnodes.nodeName !='#text':
        print("-->",childnodes.nodeName,childnodes.nodeValue)
        newnode=self.newdoc.createElement(childnodes.nodeName)
        newroot.appendChild(newnode)

        attr=childnodes.attributes.values()
        for childattr in attr:
          # print(childattr.name)

          newroot.setAttribute(childattr.name,childattr.value)#b64(childattr.value).base64encode()
          # newroot.appendChild(text)
        # value=collection.getElementsByTagName(childnodes.nodeName)[0].childNodes[0].nodeValue
        # print(value)
        # text = self.newdoc.createTextNode(b64(childnodes.nodeValue).base64encode())
        # newroot.appendChild(text)
        # newnodename.setAttribute(attrs,b64(listattr[node][attrs]).base64encode())
        # nndd=self.node.getElementsByTagName(childnodes.nodeName)[0].childNodes
        # print("nndd>>",nndd)
        self.loopxml(childnodes,self.newdoc,newnode)
     
    print(self.newdoc.toxml().replace('&quot;','\"'))     

path=r'E:\python-workspace\WebServiceInterface\ckw2016\testxml\ipkz.xml'
rb=rebuildcode(path)
rexml=rb.rebuild()
