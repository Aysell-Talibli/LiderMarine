from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('service/<slug:slug>', views.service_detail, name='service_detail'),
    path('products', views.products, name='products'),
    path('products/<str:category_name>', views.products, name='product_category'),
    path('services/<str:category_name>', views.service, name='service_category'),
    path('product/<slug:slug>', views.product_detail, name='product_detail'),
    path('contact', views.contact, name='contact'),
]