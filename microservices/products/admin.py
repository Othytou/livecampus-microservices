from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Products


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	pass


admin.site.register(Products, ProductAdmin)
