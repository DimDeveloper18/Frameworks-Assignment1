from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='products_store-index'),
    path('tools/', views.tools, name='products_store-tools'),
    path('contact/', views.contact, name='products_store-contact'),
    path('delivery/', views.delivery, name='products_store-delivery'),
    path('register/', views.reg_form, name='customers-reg_form'),
]