from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]

class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]
