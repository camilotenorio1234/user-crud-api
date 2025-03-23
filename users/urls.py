from django.urls import path
from .views import UsuarioAPIView

urlpatterns = [
    path('usuarios/', UsuarioAPIView.as_view()),                  # GET all, POST
    path('usuarios/<int:cedula>/', UsuarioAPIView.as_view()),     # GET, PUT, DELETE
]
