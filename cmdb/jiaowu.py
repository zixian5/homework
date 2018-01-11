import urllib.request,urllib.parse,urllib
import http.cookiejar
import  re
def grade():
 data=urllib.parse.urlencode([
    ('zjh','201592089'),('mm','19971020')])
 req=urllib.request.Request('http://zhjw.dlut.edu.cn/loginAction.do')
 req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  )
 cj=http.cookiejar.CookieJar()
 opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
 f=opener.open(req,data=data.encode('utf-8'))
 #print(f.read().decode('gbk'))
 #print(cj)
 req0 = urllib.request.Request('http://zhjw.dlut.edu.cn/gradeLnAllAction.do?type=ln&oper=fa')
 g= opener.open(req0)
 htmls=g.read().decode('gbk')
 url=[]
 from html.parser import HTMLParser
 class myhtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=='iframe':
           for attr in attrs:
               if(attr[0]=='src'):
                   url.append(attr[1])
 mps=n=myhtmlparser()
 mps.feed(htmls)
 #print(url)
 url='http://zhjw.dlut.edu.cn/'+url[0]
 g=opener.open(url)
 finalhtml=g.read().decode('gbk')
 da=[]
 class tdparser(HTMLParser):
    ta=0
    def handle_starttag(self, tag, attrs):
        self.ta=0
        if(tag=='td' or tag=='p'):
            for att in attrs:
                if(att[0]=='align' and att[1]=='center'):
                    self.ta=1
    def handle_data(self, data):
        if(self.ta!=0):
            da.append(str.strip(data))
 finalparser=tdparser()
 finalparser.feed(finalhtml)
 da=list(filter(lambda x:len(x)>0,da))
 finaldata=[]
 t=[]
 for x in range(len(da)):
    t.append(da[x])
    if(len(t)==3):
        if(re.match('^\d',da[x+1])):
            t.append('')
    if(len(t)==7):
        finaldata.append(t)
        t=[]
 return finaldata
grade()
