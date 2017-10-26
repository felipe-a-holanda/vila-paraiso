from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from website.forms import ContactForm
from website.models import Contact

class ContactView(CreateView):
    template_name = 'soon.html'
    form_class = ContactForm
    success_url = reverse_lazy('website:thanks-view')
    
    def get_success_url(self):
        return reverse_lazy('website:thanks-view',args=(self.object.id,))

class ThanksView(DetailView):
    model = Contact
    template_name = 'thanks.html'

