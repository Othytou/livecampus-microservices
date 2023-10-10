from django.urls import re_path, path

from . import api

urlpatterns = [

	path('listing/', api.product_listing),
	path('<int:id_product>/', api.product_only),
	path('add_product/', api.add_product),
	# path('<int:id_product>/update/', api.product_update),
	path('<int:id_product>/delete/', api.product_delete),
]
