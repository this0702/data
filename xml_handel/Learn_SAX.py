import xml.sax#引入API
#先生成一个ContentHandler处理器
class EnumHandle(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData=''
        self.name=''#枚举字段名称
        self.class_name=''#枚举字段编码
        self.enum_name=''#枚举值
        self.enum_no=''#枚举序号
    #开始事件
    def startElement(self,tag,attribute):
        self.CurrentData=tag
        if(tag=='Enumerate'):
            print(attribute['displayName']+'('+(attribute['fullClassName']).split('.')[-1]+')')
        if(tag=='enumitem'):
            print(attribute['enumValue']+'='+attribute['enumDisplay'])

    def endElement(self, tag):
        print('end')
    def characters(self, content):
        print('current')

# 创建一个 XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
# 重写 ContextHandler
Handler = EnumHandle()
parser.setContentHandler(Handler)
parser.parse("cost.xml")