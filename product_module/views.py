from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product_module.models import Product


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['products'] = Product.objects.filter(is_active=True).all()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_module/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = Product.objects.filter(is_active=True)
        return context
