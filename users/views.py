from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioAPIView(APIView):

    def get(self, request, cedula=None):
        if cedula:
            try:
                usuario = Usuario.objects.get(cedula=cedula)
                serializer = UsuarioSerializer(usuario)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            usuarios = Usuario.objects.all()
            serializer = UsuarioSerializer(usuarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, cedula):
        try:
            usuario = Usuario.objects.get(cedula=cedula)
        except Usuario.DoesNotExist:
            return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario actualizado exitosamente'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cedula):
        try:
            usuario = Usuario.objects.get(cedula=cedula)
            usuario.delete()
            return Response({'message': 'Usuario eliminado exitosamente'}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
