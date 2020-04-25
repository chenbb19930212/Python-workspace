from xml.dom.minidom import parse
from xml.dom.minidom import Document
import xml.dom.minidom
from base64code import base64code as b64

class rebuildcode(object):
  """docstring for ClassName"""
  def __init__(self, xmlpath,codetype):
    # super(ClassName, self).__init__()
    self.xmlpath = xmlpath
    if codetype !='':
      self.codetype = codetype
    else:
      self.codetype='utf-8'

  def rebuild(self):
    # DOMTree = xml.dom.minidom.parse(r'C:\Users\Lenovo\Desktop\xml111.xml')
     ##解析xml
    try:
      DOMTree = xml.dom.minidom.parse(self.xmlpath)
    except Exception as e:
      DOMTree = xml.dom.minidom.parseString(self.xmlpath)

      
    collection = DOMTree.documentElement
    # print("主节点：",collection.nodeName)#主节点名
    ##创建新的xml
    newdoc=Document()
    newroot=newdoc.createElement(collection.nodeName)
    newdoc.appendChild(newroot)
    #循环解析xml并同步创建新xml并base64加密
    self.loopxml(collection,newdoc,newroot)
    newxml=newdoc.toxml().replace('&quot;','\"')
    return b64(newxml,self.codetype).base64encode()
    
  def loopxml(self,collection,newdoc,newroot):
    self.node=collection
    self.newdoc=newdoc
    self.newroot=newroot
    #获取节点的下的 所有子节点
    for childnodes in self.node.childNodes:
      if childnodes.nodeName =='#text':#python中节点的childNodes 包换nodevalue值和 子节点信息 。
        #有换行符和空格的
        # value=childnodes.nodeValue
        # text = self.newdoc.createTextNode(b64(value).base64encode()) #b64(value).base64encode()
        # newroot.appendChild(text)
        #无换行符和空格的
        if childnodes.nodeValue.strip()!='':
          value=childnodes.nodeValue
          if value=='pdf':
            value=self.getpdf()
          text = self.newdoc.createTextNode(b64(value,self.codetype).base64encode()) #b64(value).base64encode()
          newroot.appendChild(text)
          # print("#text:",childnodes.nodeValue.strip())
       
      if childnodes.nodeName !='#text':
        # print("-->",childnodes.nodeName,childnodes.nodeValue)
        #获取节点的节点名并在新xml里创建此节点名
        newnode=self.newdoc.createElement(childnodes.nodeName)
        newroot.appendChild(newnode)

        #获取节点的属性(attr)信息
        attr=childnodes.attributes.values()
        for childattr in attr:
          # print(childattr.name)
          #新xml添加属性信息
          newnode.setAttribute(childattr.name,b64(childattr.value,self.codetype).base64encode())#b64(childattr.value).base64encode()
        self.loopxml(childnodes,self.newdoc,newnode)

  def getpdf(self):
    pdffile=r'D:/result.pdf'
    f= open(pdffile,'rb') 
    data=f.read()
      # nr=content.rstrip()
    # print(bytes.decode(data))
    # print(data)
    # print('-->',b64(str(data) ,self.codetype).base64encode())
    return data




# path=r'E:\python-workspace\WebServiceInterface\ckw2016\testxml\ipkz.xml'
# rb=rebuildcode(path)
# rexml=rb.rebuild()
# print(rexml)