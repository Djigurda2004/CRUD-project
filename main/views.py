from django.shortcuts import render

def index(request):
    data={'title':'Main Page',
          'values':['Some text','Hello','123'],
          'obj' : {
              'car': 'Mercedes CLS 63',
              'acs': 'Mag Shar#2',
              'house': 'House 1488'
          }         
    }
    return render(request, "main/index.html",data)

def about(request):
    return render(request, "main/about.html")

def more(request):
    return render(request,"main/more.html")