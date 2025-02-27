from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib import messages
from datetime import date


from mein.forms import ContactForm



class Index_View(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bugun'] = date.today().strftime('%d-%m-%Y')  # Bugungi sana  
        return context
            



class Category_View(TemplateView):
    template_name = 'category.html'



class Contact_View(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bugun'] = date.today().strftime('%d-%m-%Y')  # Bugungi sana 
        context['form'] = ContactForm()
        return context



class Single_View(TemplateView):
    template_name = 'single.html'
