from django.urls import re_path, path

from . import views

urlpatterns = [
	path('listing/', views.product_list, name='product_listing'),
	path('product/<pk:id>/', views.product_get,),
	path('add_product/', views.product_add,),
	path('update_product/<pk:id>/', views.product_update),
	path('delete_product/<pk:id>/', views.product_delete),
]
