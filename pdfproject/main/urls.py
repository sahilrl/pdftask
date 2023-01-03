from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name=None),
    path('report1/', views.report1, name='portrait'),
    path('report2/', views.report2, name='landscape')
]
