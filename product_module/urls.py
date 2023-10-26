from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list_page'),
    path('<slug:slug>', views.ProductDetail.as_view(), name='product_detail_page')
]
