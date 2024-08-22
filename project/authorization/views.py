from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

class UserRegisterView(generics.CreateAPIView):
	serializer_class = UserSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)

class CurrentUserView(generics.RetrieveAPIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data)