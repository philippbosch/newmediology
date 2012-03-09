from django.views.generic import DetailView

from .models import Page


class PageView(DetailView):
    model = Page
    template_name = "pages/default.html"
