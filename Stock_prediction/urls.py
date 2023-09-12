from django.contrib import admin
from django.urls import path, include
from app_prediction.views import home, api_predict
from app_prediction import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('app_prediction/', include('app_prediction.urls')),
    path('', home, name='home'),
    path('api/predict', views.api_predict, name='predict'),
]