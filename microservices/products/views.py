from django.shortcuts import render
from .models import Products


def product_list(request):
	context = {
		'title_page': 'Produits',
	}
	return render(request, 'products/list.html', context)

def product_get(request, product_id):
	product = Products.objects.get(pk=product_id)
	return render(request, 'products/product.html')

def product_add(request):
	product = Products.objects.create()
	return render(request, 'products/add_product.html')

def product_update(request, product_id):
	product = Products.objects.update(pk=product_id)
	return render(request, 'productss/product_update.html')

def product_delete(request, product_id):
	product = Products.objects.delete(pk=product_id)
	return render(request, 'productss/product_delete.html')

