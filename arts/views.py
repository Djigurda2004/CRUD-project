from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def arts(request):
    arts = Articles.objects.all()
    return render(request,'arts/articles.html',{'arts':arts})


class ArtDetailView(DetailView):
    model = Articles
    template_name = "arts/details_view.html"
    context_object_name = 'article'


class ArtUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Articles
    template_name = "arts/addart.html"
    form_class = ArticlesForm
    raise_exception = True
    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user


class ArtDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Articles
    success_url = '/arts/'
    template_name = "arts/art_delete.html"
    raise_exception = True
    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user


@login_required
def add_art (request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
        else:
            error = 'The form is incorrect'
    form = ArticlesForm()
    data = {
        'form' : form,
        'error' : error}
    return render(request,'arts/addart.html',data)