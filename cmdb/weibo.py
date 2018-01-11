import urllib.request,urllib.parse,urllib
import gzip,string
def get():
 req=urllib.request.Request('https://weibo.com/a/hot/realtime')
 req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
 req.add_header('Accept-Encoding','gzip, deflate, sdch, br')
 req.add_header('Connection','keep-alive')
 req.add_header('Cookie','SINAGLOBAL=1845607129643.2253.1505545085759; SUB=_2AkMuuOzsf8NxqwJRmP4UzWvmboV1yADEieKY5B03JRMxHRl-yT83qlNctRBVZOiaLiof28OmcL47rV0G9WnEYA..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWB8qBNc6_ulA_Pc8jsS9g2; UM_distinctid=15ff8d1755831-02f34398896ade-323f5c0f-100200-15ff8d1755b15b; _s_tentry=www.baidu.com; Apache=9653766422744.625.1514984711054; ULV=1514984711060:32:2:2:9653766422744.625.1514984711054:1514982973452; YF-V5-G0=bb389e7e25cccb1fadd4b1334ab013c1; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; YF-Page-G0=23b9d9eac864b0d725a27007679967df; wb_cusLike_3655689037=N; login_sid_t=1546a2bd6cca6f9fa2fd2d605657c305; cross_origin_proto=SSL; UOR=baike.baidu.com,widget.weibo.com,www.baidu.com; WBStorage=c1cc464166ad44dc|undefined')
 f=urllib.request.urlopen(req)
 #print(gzip.decompress(f.read()).decode('utf8'))
 html=gzip.decompress(f.read()).decode('utf8')
 list=[]
 from html.parser import HTMLParser
 class myhtmlparser(HTMLParser):
    ta=0
    da=[]
    num=0
    def handle_starttag(self, tag, attrs):
        self.ta=0
        self.da=[]
        if (tag == 'a'):
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'S_txt1':
                    self.ta=1
        if (self.ta !=0):
            for attr in attrs:
                if attr[0]=='href':
                    self.da.append('https://weibo.com/a/hot/'+attr[1])
                if (str(attr[1]).find('weibo')!=-1):
                    self.ta=0
    def handle_data(self, data):
        if (self.ta!=0):
            self.da.append(data)
            self.num+=1
            if(self.num&2==0 ):
             list.append(self.da)
 finalparser=myhtmlparser()
 finalparser.feed(html)
 return list
get()