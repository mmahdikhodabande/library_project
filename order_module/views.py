from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from order_module.models import Order, OrderDetail
from product_module.models import Product


def add_to_order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    # if count < 1:
    #     count = 1

    product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()

    if request.user.is_authenticated:
        if product is not None:

            current_order, created = Order.objects.get_or_create(is_pain=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول شما با موفقیت به سبد خرید اضافه شد',
                'confirmButtonText': 'باشه مچکرم',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر شما یافت نشد',
                'confirmButtonText': 'ممنونم',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای سفارش محصول باید حتما لاگین کنید',
            'confirmButtonText': 'حتما',
            'icon': 'error'
        })


def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_pain=False,
                                                                                             user_id=request.user.id)

    total_amount = 0
    for order_detail in current_order.orderdetail_set.all():
        total_amount += order_detail.product.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'order_module/order_page.html', context)
