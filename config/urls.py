"""config URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('', include('shop.urls', namespace='shop')),
    path('about/', include('shop.urls', namespace='shop')),
    path('contact/', include('shop.urls', namespace='shop')),
    path('back/', include('shop.urls', namespace='shop')),
    path('delivery/', include('shop.urls', namespace='shop')),
    path('question/', include('shop.urls', namespace='shop')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
