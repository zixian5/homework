import urllib.request,urllib.parse,urllib
def get():
 req=urllib.request.Request('https://daily.zhihu.com/')
 f=urllib.request.urlopen(req)
 html=f.read().decode('utf8')
 #print(f.read().decode('utf8'))
 from html.parser import HTMLParser
 da=[]
 class aHtmlParser(HTMLParser):
    ta=0
    def handle_starttag(self, tag, attrs):
        ta=0
        if(tag=='a'):
            for attr in attrs:
                if (attr[0]=='class' and attr[1]=='link-button'):
                    self.ta=1
        if(self.ta !=0):
            for attr in attrs:
               if(attr[0]=='href'):
                 da.append('https://daily.zhihu.com'+attr[1])
    def handle_data(self, data):
        if (self.ta !=0):
            da.append(data)
 myParser=aHtmlParser()
 myParser.feed(html)
 data=[]
 i=1
 t=[]
 for x in da :
   if(str(x).find('java')!=-1):
       break
   t.append(x)
   if(i%2==0):
       data.append(t)
       t=[]
   i+=1
 return data