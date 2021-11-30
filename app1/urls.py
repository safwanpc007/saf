from django.urls import path
from . import views 

app_name='app1'


urlpatterns = [
    path('',views.home,name='haii'),
    # path('home',views.one,name='hello'),

]