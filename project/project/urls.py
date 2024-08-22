from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('authorization.urls', namespace='authorization')),
	path('api/', include('marketplace.urls', namespace='marketplace')),
]
