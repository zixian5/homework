from django.shortcuts import render
from django.shortcuts import  HttpResponse
from cmdb import models
from cmdb import jiaowu
from cmdb import weibo,zhihuribao,basketball
# Create your views here.
def index(request):
    context ={}
    context['hello']="hello world!"
    return render(request,'hello.html',context)

def testdb(request):
    test1=models.user(age=10,name='hello',user_name='helo')
    test1.save()
    return HttpResponse("插入数据成功")
def get(request):
    return HttpResponse(str(request.GET['test']))
def help(request):
    data=jiaowu.grade()
    context={}
    context['data']=data
    return render(request,'jiaowu.html',context)
def wei(request):
    data=[]
    da=weibo.get()
    b=1
    for x in da:
        i=0
        t=[]
        t.append(b)
        t.append(x[1])
        t.append(x[0])
        data.append(t)
        b+=1
    context = {}
    context['data'] = data
    return render(request, 'weibo.html', context)
def zhi(request):
    data = []
    da = zhihuribao.get()
    b = 1
    for x in da:
        i = 0
        t = []
        t.append(b)
        t.append(x[1])
        t.append(x[0])
        data.append(t)
        b += 1
    context = {}
    context['data'] = data
    return render(request, 'zhihu.html', context)
def nbainf(request):
    data = []
    da = basketball.get()
    b = 1
    for x in da:
        i = 0
        t = []
        t.append(b)
        t.append(x[1])
        t.append(x[0])
        data.append(t)
        b += 1
    context = {}
    context['data'] = data
    return render(request, 'nba.html', context)