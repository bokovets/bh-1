from django.views.generic import ListView, TemplateView


from .models import Post
# Create your views here.



class HomePagePost(ListView):
    model = Post
    template_name = 'home_post.html'
    context_object_name = 'all_post_list'







