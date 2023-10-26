from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list_page'),
    path('product-detail', views.DetailView.as_view(), name='product_detail_page')
]
