from django.urls import path
from webapp import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('result/', views.result, name = 'result'),
    path('prediction/', views.prediction, name="prediction"),
    path('mypanel/', views.mypanel, name="mypanel"),
    path('error/', views.error, name="error"),
    
]
