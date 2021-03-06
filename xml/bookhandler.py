
import xml.sax
import pprint
import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):
  def __init__(self):
    self.inTitle = 0
    self.mapping = {}
 
  def startElement(self, name, attributes):
    if name == "book":
      self.buffer = ""
      self.isbn = attributes["isbn"]
    elif name == "title":
      self.inTitle = 1
 
  def characters(self, data):
    if self.inTitle:
      self.buffer += data
 
  def endElement(self, name):
    if name == "title":
      self.inTitle = 0
      self.mapping[self.isbn] = self.buffer
      

parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse("C:\\Users\\AngelintheWoods\\Desktop\\XML\\bookhandler.xml")
pprint.pprint(handler.mapping)


