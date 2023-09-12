from django.urls import path
from .views import  home, api_predict, faq, about
from . import views
urlpatterns = [
    
    path('api/predict', views.api_predict, name='predict'),
    path('', home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
]
