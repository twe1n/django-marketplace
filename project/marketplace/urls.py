from django.urls import path

from .views import product_list, product_detail

app_name = 'marketplace'
urlpatterns = [
	path('products/', product_list, name='product-list-create'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
]