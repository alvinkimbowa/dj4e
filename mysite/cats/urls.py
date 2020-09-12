from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('lookup/', views.BreedView.as_view(), name='breed_list'),
    path('lookup/create/', views.BreedCreateView.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.BreedUpdateView.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedDeleteView.as_view(), name='breed_delete'),
    path('main/create/', views.CatCreateView.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdateView.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDeleteView.as_view(), name='cat_delete'),
]