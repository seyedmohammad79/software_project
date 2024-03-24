from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView

from contact_module.forms import ContactUsForm


# Create your views here.

class ContactUsVIew(CreateView):
    form_class = ContactUsForm
    template_name = ''
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['site_setting'] = ''
        return context
