import urllib.request,urllib.parse,urllib
import gzip,string

def get():
 req=urllib.request.Request('https://news.zhibo8.cc/nba/more.htm')
 f=urllib.request.urlopen(req)
 htm=f.read().decode('utf-8')
 #print(f.read().decode('utf-8'))
 from html.parser import HTMLParser
 da=[]
 class parser(HTMLParser):
    ta=0
    d=[]
    def handle_starttag(self, tag, attrs):
        self.d=[]
        self.ta=0
        if tag == 'a':
            self.ta=1
        if(self.ta!=0):
            for attr in attrs:
                #print(attr)
                if (attr[0]=='href'):
                    if(str(attr[1]).find('news.zhibo8.cc')==-1):
                        self.ta=0
                    else:
                        self.d.append('https:'+attr[1])
    def handle_data(self, data):
        if(self.ta!=0):
            self.d.append(data)
            da.append(self.d)
 p=parser()
 p.feed(htm)
 return da
