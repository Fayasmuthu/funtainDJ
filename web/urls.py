from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("about/", TemplateView.as_view(template_name="web/about.html")),
    # path("contact/", views.contact, name="contact"),
]
