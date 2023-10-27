from django.shortcuts import render
from django.views.generic import CreateView
from .models import ContactUsModel
from .forms import ContactUsForm


# Create your views here.


def contact_page(request):
    return render(request, 'contact_module/contact_us_page.html')


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    model = ContactUsModel
    form_class = ContactUsForm
    success_url = '/contact-us/'
    context_object_name = 'form'
