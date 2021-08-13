from django.urls import path
from app2 import views
app_name='application2'
urlpatterns=[
    path('app2_fun/',views.app2_fun,name='app2_fun')
]