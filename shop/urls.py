from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('back/', views.back, name='back'),
    path('delivery/', views.delivery, name='delivery'),
    path('question/', views.question, name='question'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]