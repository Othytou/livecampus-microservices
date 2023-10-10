from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Products


def product_listing(request):
	if request.method == 'GET':
		data = []
		try:
			products = Products.objects.all().values('id', 'Name', 'Quantity', 'Price', 'DISPONIBILITE')
		except Exception as e:
			data.append(str(e))
		else:
			for product in products:
				data.append(product)
		return JsonResponse({'data': data})

	else:
		return HttpResponse('Cette méthode n\'est pas autorisé', status=405)


def product_only(request, id_product):
	if request.method == 'GET':
		data = []
		try:
			product = Products.objects.get(pk=id_product)
			product_fields = product.__dict__


		except Products.DoesNotExist:
			text = 'Le produit spécifié n\'existe pas'
			data.append(text)
		except Exception as e:
			text = 'Erreur lors l\'affichage du Produit'
			data.append(text, str(e))
		else:
			product_fields = {
				key: value
				for key, value in product.__dict__.items()
				if not key.startswith('_')
			}

			data.append(product_fields)
		return JsonResponse({'data': data})
	else:
		return render(request, 'base/405.html', status=405)


@csrf_exempt
def add_product(request):
	if request.method == 'POST':
		data = []
		text = ''
		req = request.POST
		try:
			product = Products.objects.create(
				Name=req['name'], Quantity=req['quantity'], Price=req['price'], DISPONIBILITE=req['available'])
		except Exception as e:
			text = 'Erreur lors de la création du Produit'
			data.append((text, {'erreur': str(e)}))
		else:
			text = f'Création du Produit : {product.Name}'
			data.append(text)
		return JsonResponse({'data': data})
	else:
		return render(request, 'base/405.html', status=405)


# if HttpResponse == 403:
# 	return render(request, 'base/405.html', status=405)

# @csrf_exempt
# def product_update(request, id_product):
# 	if request.method == 'PUT':
# 		req = request.PUT
# 		data = []
# 		try:
# 			product = Products.objects.get(pk=id_product)
# 			product.update(
# 				Name=req['name'], Quantity=req['quantity'], Price=req['price'], DISPONIBILITE=req['available'])
# 		except Exception as e:
# 			text = 'Erreur lors de la modification du Produit'
# 			data.append(text, str(e))
# 		else:
# 			text = f'Modification du Produit : {product.Name}'
# 			data.append(text)
# 		return JsonResponse({'data': data})
# 	else:
# 		return render(request, 'base/405.html', status=405)

@csrf_exempt
def product_delete(request, id_product):
	if request.method == 'DELETE':
		data = []
		try:
			product = Products.objects.get(pk=id_product)
			product.delete()
			text = f'Suppression du Produit : {product.Name}'
			data.append(text)
		except Products.DoesNotExist:
			text = 'Le produit spécifié n\'existe pas'
			data.append(text)
		except Exception as e:
			text = 'Erreur lors de la suppression du Produit'
			data.append(text, str(e))
		return JsonResponse({'data': data})
	else:
		return render(request, 'base/405.html', status=405)
