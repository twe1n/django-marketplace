from django.urls import path

from .views import UserRegisterView, CurrentUserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'authorization'
urlpatterns = [
	path('current-user/', 		CurrentUserView.as_view(), 			name='current_user'),		# Информация о пользователе по токену
	path('register/', 			UserRegisterView.as_view(), 		name='register'),			# Регистрация пользователя
	path('token/', 				TokenObtainPairView.as_view(), 		name='token_obtain_pair'),	# Получение токена
	path('token/refresh/', 		TokenRefreshView.as_view(), 		name='token_refresh'),		# Обновление токена
]