from django.urls import path

from .views import ProductListAPIView, ProductAPIView

app_name = 'marketplace'
urlpatterns = [
	path('products/', ProductListAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
]