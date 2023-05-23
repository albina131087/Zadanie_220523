from django.urls import path

# from .views import homePageView

from .views import CatalogListView, CatalogDetailView, CatalogCreateView, CatalogUpdateView, CatalogDeleteView

urlpatterns = [
    path('film/<int:pk>/delete/', CatalogDeleteView.as_view(), name='film_delete'),
    path('film/<int:pk>/edit/', CatalogUpdateView.as_view(), name='film_edit'),
    path('film/new/', CatalogCreateView.as_view(), name='film_new'),
    path('film/<int:pk>/', CatalogDetailView.as_view(), name='film_detail'),
    path('', CatalogListView.as_view(), name='home')
]