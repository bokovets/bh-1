from django.urls import path

from . import views 



urlpatterns = [
    path('',  views.homePageView.as_view(), name ='home'),
    path('about/', views.AboutPageView.as_view(), name = 'about' ),
    path('about/description/', views.AboutDescription.as_view(), name = 'description' ),
]