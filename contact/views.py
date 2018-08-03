from django.views.generic.edit import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.contrib import messages

class ContactAdd(CreateView):
    model = Contact
    fields = ['name','email','phone','message']
    success_url = reverse_lazy('contact-page')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,'Mensaje recibido exitosamente')
        return super().form_valid(form)
