
from django.views.generic import TemplateView
# Create your views here.




class homePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class AboutDescription(TemplateView):
    template_name = 'desriptionofabout.html'