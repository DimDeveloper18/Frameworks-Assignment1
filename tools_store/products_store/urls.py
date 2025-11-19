from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='products_store-index'),
    path('tools/', views.tools, name='products_store-tools'),
    path('contact/', views.contact, name='products_store-contact'),
    path('delivery/', views.delivery, name='products_store-delivery'),
    path('register/', views.reg_form, name='products_store-reg_form'),
    path('login/', auth_views.LoginView.as_view(template_name='products_store/login.html'), name='products_store-login'),
]