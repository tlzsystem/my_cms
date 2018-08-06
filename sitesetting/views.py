from django.views.generic.edit import CreateView
from .models import SiteSetting
from django.urls import reverse_lazy

class SettingSite(CreateView):
    model = SiteSetting
    fields = ['name', 'description', 'keywords', 'author', 'title','twitter','github','linkedin', 'mail']
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.site='app'
        return super().form_valid(form)

