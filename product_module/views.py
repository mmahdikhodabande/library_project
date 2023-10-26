from django.shortcuts import render
from django.views.generic import DetailView, ListView

from product_module.models import Product


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['products'] = Product.objects.filter(is_active=True).all()
        return context


class ProductDetailView(DetailView):
    pass
