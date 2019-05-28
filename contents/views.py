from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

# Create your views here.
class Hello(View):

    def get(self,request):
        context = {"message": "helloWorld"}
        return TemplateResponse(request, "./hello.html", context)
hello = Hello.as_view()