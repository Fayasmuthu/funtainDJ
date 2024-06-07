import json
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from django.http import JsonResponse


from .models import Blog,Categories
from .forms import ContactForm


class IndexView(TemplateView):
    template_name = "web/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_index"] = True
        context["categories"] = Categories.objects.filter(is_active=True)
        context["blog"] = Blog.objects.filter(is_active=True)
        context["form"] = ContactForm() 
        return context

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = self.get_context_data()
            messages.success(request, "Message successfully submitted.")
            return redirect('/')
        else:
            messages.error(request, "Form validation error.")
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)



