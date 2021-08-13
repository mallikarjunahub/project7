from django.urls import path
from app1 import views
app_name='application1'
urlpatterns=[
    path('app1_fun/',views.app1_fun,name='app1_fun')
]