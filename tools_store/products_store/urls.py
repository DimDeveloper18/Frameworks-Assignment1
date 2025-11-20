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
    path('logout/', auth_views.LogoutView.as_view(template_name='products_store/logout.html'), name='products_store-logout'),
    path('basket/', views.basket_page, name='products_store-basket_page'),
    path('comments_view/', views.comments_view, name='products_store-comments-view'),
    path('profile/', views.profile_page, name='products_store-profile_page'),
]