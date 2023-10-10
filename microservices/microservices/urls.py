from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="base/base.html"), name='home'),
    path('products/', include(('products.urls', 'products'), namespace='products')),

    path('admin/', admin.site.urls)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
