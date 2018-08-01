from django.views.generic.edit import CreateView
from .models import Contact
from django.urls import reverse_lazy

class ContactAdd(CreateView):
    model = Contact
    fields = ['name','email','phone','message']
    success_url = reverse_lazy('contact-page')
