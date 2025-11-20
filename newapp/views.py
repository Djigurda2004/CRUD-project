from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView,UpdateView,DeleteView

def newapp_home(request):
    newapp = Articles.objects.all()
    return render(request,'newapp/newapp_home.html',{'newapp':newapp})

class NewappDetailView(DetailView):
    model = Articles
    template_name = "newapp/details_view.html"
    context_object_name = 'article'

class NewappUpdateView(UpdateView):
    model = Articles
    template_name = "newapp/addapp.html"
    form_class = ArticlesForm

class NewappDeleteView(DeleteView):
    model = Articles
    success_url = '/newapp/'
    template_name = "newapp/newapp_delete.html"

def addapp (request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'The form is incorrect'
    
    form = ArticlesForm()
    
    data = {
        'form' : form,
        'error' : error}
    
    return render(request,'newapp/addapp.html',data)