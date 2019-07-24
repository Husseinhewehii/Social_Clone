from django.views.generic import TemplateView

class Home_View(TemplateView):
    template_name = 'index.html'

class Test_Page(TemplateView):
    template_name = 'test.html'

class Thanks_Page(TemplateView):
    template_name = 'thanks.html'