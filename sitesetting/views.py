from django.views.generic.edit import UpdateView
from .models import SiteSetting
from django.urls import reverse_lazy

class SiteSettingEdit(UpdateView):
    model = SiteSetting
    fields = ['name','description','keywords','author','title','twitter','github','linkedin','mail']
    success_url = reverse_lazy('dj-admin-view')
    def get_object(self, queryset=None):
        return SiteSetting.objects.get(pk='app')