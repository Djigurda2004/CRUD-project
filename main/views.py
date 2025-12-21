from django.shortcuts import render

def index(request):
    data={'title':'Main Page',
          'values':['Some text','H'],
          'obj' : {
              "data":403
          }         
    }
    return render(request, "main/index.html",data)

def about(request):
    return render(request, "main/about.html")

def more(request):
    return render(request,"main/more.html")