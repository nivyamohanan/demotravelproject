
from django.urls import path

from . import views

urlpatterns = [

    path('',views.operations,name="operations")

   # path('add/sub/mul/div',views.result,name="result"),
    #path('Home',views.Home,name="Home"),
    # path('About',views.About,name="About"),
    #path('Details', views.Details, name="Details"),
    #path('contact',views.contact,name="contact")

]