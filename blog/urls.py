from django.urls import path

from . import views




urlpatterns = [
   
    path('', views.BlogListView.as_view(), name = 'blog' ),
    path('postblog/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
]