from django.shortcuts import render,redirect
from django.views.generic import TemplateView


class Index_View(TemplateView):
    template_name = 'index.html'



class Category_View(TemplateView):
    template_name = 'category.html'



class Contact_View(TemplateView):
    template_name = 'contact.html'



class Single_View(TemplateView):
    template_name = 'single.html'
