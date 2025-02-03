from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('medidas.urls')),  # Incluye las rutas de la app "medidas".
]
