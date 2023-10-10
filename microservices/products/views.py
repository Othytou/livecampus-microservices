from django.shortcuts import render
from .models import Products


def product_list(request):
	products = Products.objects.all()
	return render(request, 'product/list.html')

def product_get(request, product_id):
	product = Products.objects.get(pk=product_id)
	return render(request, 'product/product.html')

def product_add(request):
	product = Products.objects.create()
	return render(request, 'product/add_product.html')

def product_update(request, product_id):
	product = Products.objects.update(pk=product_id)
	return render(request, 'product/product_update.html')

def product_delete(request, product_id):
	product = Products.objects.delete(pk=product_id)
	return render(request, 'product/product_delete.html')

