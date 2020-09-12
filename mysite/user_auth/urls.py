from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'user_auth'

urlpatterns = [
    path('', TemplateView.as_view(template_name='user_auth/main.html'), name='index'),
    path('python', views.DumpPython.as_view(), name='python'),
]