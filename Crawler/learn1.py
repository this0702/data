import scrapy
from scrapy import Selector
class NgaSpider(scrapy.Spider):
    name = "NgaSpider"
    host = "http://bbs.ngacn.cc/"
    # start_urls是我们准备爬的初始页
    start_urls = ["http://bbs.ngacn.cc/thread.php?fid=406"]

    # 这个是解析函数，如果不特别指明的话，scrapy抓回来的页面会由这个函数进行解析。
    # 对页面的处理和分析工作都在此进行，这个示例里我们只是简单地把页面内容打印出来。
    def parse(self, response):
        selector = Selector(response)
        # 在此，xpath会将所有class=topic的标签提取出来，当然这是个list
        # 这个list里的每一个元素都是我们要找的html标签
        content_list = selector.xpath("//*[@class='topic']")
        # 遍历这个list，处理每一个标签
        for content in content_list:
            # 此处解析标签，提取出我们需要的帖子标题。
            topic = content.xpath('string(.)').extract_first()
            print(topic)
            # 此处提取出帖子的url地址。
            url = self.host + content.xpath('@href').extract_first()
            print (url)
