from django.views.generic import TemplateView
from post.models import Post

class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_posts'] = Post.objects.all()[:5]
        return context