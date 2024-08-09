from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Adicionada a vírgula
    path('usuarios/', include('usuarios.urls')),  # Incluído o 'include'
    path('empresarios/', include('empresarios.urls')),
]
