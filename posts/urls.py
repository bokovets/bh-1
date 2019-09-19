from django.urls import path

from . import views 


urlpatterns = [
    
    path('', views.HomePagePost.as_view(), name = 'post' ),
]