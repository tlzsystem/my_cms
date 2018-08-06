from django.views.generic.edit import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect
import json
import urllib

class ContactAdd(CreateView):
    model = Contact
    fields = ['name','email','phone','message']
    success_url = reverse_lazy('contact-page')

    def form_valid(self, form):
        recaptcha_resp = self.request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        datos={
            'secret': settings.GOOGLE_SECRET_KEY,
            'response': recaptcha_resp
        }
        data = urllib.parse.urlencode(datos).encode()
        reqs = urllib.request.Request(url, data)
        response = urllib.request.urlopen(reqs)
        result = json.loads(response.read().decode())

        if result['success']:
            messages.add_message(self.request, messages.SUCCESS,'Mensaje recibido exitosamente')
            return super().form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR,'Captcha inválido')
            return redirect('contact-page')
