from django.shortcuts import render 
from apk.serializers import ProductSerializers
from apk.models import Product
from rest_framework.response import Response # type: ignore
from django.http import JsonResponse
from rest_framework.decorators import api_view
from apk.serializers import ProductSerializers, OrderSerializer
from apk.models import Product, Order, CustomUser


# Create your views here.

@api_view(['GET'])
def product_list(request):
	products = Product.objects.all()
	serializers = ProductSerializers(products, many = True)
	return Response(serializers.data)

@api_view(['GET'])
def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	serializers = ProductSerializers(product)
	return Response(serializers.data)

@api_view(['GET'])
def order_list(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)


def view_info(request):
    products = Product.objects.all()
    from apk.serializers import ProductInfoSerializer  # Ensure this import exists

    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']  # Corrected aggregate usage
    })
    return Response(serializer.data)
