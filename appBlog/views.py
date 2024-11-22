from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
from django.urls import reverse_lazy 
from django.views.generic import ListView,CreateView,UpdateView,DeleteView 
from appBlog.forms import BlogForm
from appBlog.models import BlogPost 
 
class BlogView(ListView): 
    model=BlogPost 
    #=BlogPost.objects.all() 
    context_object_name='posts'#posts à utiliser dans les pages html  
    template_name="blogView.html" 
 
class blogcreate(CreateView): 
    model = BlogPost 
   # fields=['title','content','author','created_on']# soit fields soit form class 
    form_class= BlogForm
    template_name = "blogcreate.html" 
    success_url=reverse_lazy('appBlog:listhtml') 
 
class blogUpdateView(UpdateView): 
    model = BlogPost 
   # fields = ['title', 'author','content'] 
    form_class= BlogForm
    pk_url_kwarg = 'pk' 
    template_name = "blogUpdate.html" 
    success_url=reverse_lazy('Posts:listhtml') 
 
class blogDeleteView(DeleteView): 
    model = BlogPost 
    pk_url_kwarg = 'pk' 
    template_name = "blogdelete.html" 
    success_url=reverse_lazy('Posts:listhtml') 