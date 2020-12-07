from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import blog_post
# Create your views here.


class Homeview(ListView):
    model = blog_post
    template_name = 'myapp/index.html'
    context_object_name = 'blog_posts'
    ordering =['-id']
    paginate_by = 3

class Full_view(DetailView):
    model = blog_post
    template_name = 'myapp/details.html'


class Creat_view(CreateView):
    model = blog_post
    template_name = 'myapp/creat.html'
    fields = ['title', 'text','img']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
