from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/<int:id>/', views.product_detail, name='product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('form/', views.form, name='form'),
    path('product/edit/<int:id>/', views.edit_product, name='edit_product'),
]