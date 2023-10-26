from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'home_module/index_page.html'


def site_header_references(request):
    return render(request, 'shared/site_header_references.html')


def site_header_partial(request):
    return render(request, 'shared/site_header_partial.html')


def site_footer_references(request):
    return render(request, 'shared/site_footer_references.html')


def site_footer_partial(request):
    return render(request, 'shared/site_footer_partial.html')
