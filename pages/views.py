from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pages 
from django.urls import reverse_lazy
# Create your views here.

class PageListView(ListView):
    model = Pages 
    template_name = "home.html"
    context_object_name = "pages"

class PageDetailView(DetailView):
    model = Pages 
    template_name = "detail_page.html"
    context_object_name = "page"

class PageCreateView(CreateView):
    model = Pages 
    template_name = "new_page.html"
    fields = '__all__' # какие поля мы будем заполнять в веб-форме

class PageUpdateView(UpdateView):
    model = Pages 
    template_name = "update_page.html"
    fields = ['title', 'pagebody'] # поля, которые я хочу обновлять

class PageDeleteView(DeleteView):
    model = Pages 
    template_name = "delete_page.html"
    success_url = reverse_lazy("home")