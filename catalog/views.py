from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Film

class CatalogListView(ListView):
    model = Film
    template_name = 'home.html'

class CatalogDetailView(DetailView):
    model = Film
    template_name = 'film_detail.html'

class CatalogCreateView(CreateView):
    model = Film = 'film_new.html'
    fields = '__all__'
    # какие столбцы можно создавать

class CatalogUpdateView(UpdateView):
    model = Film
    template_name = 'film_edit.html'
    fields = ['title', 'year', 'country', 'genre', 'rating']

class CatalogDeleteView(DeleteView):
    model = Film
    template_name = 'film_delete.html'
    success_url = reverse_lazy('home')