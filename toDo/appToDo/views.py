from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

from rest_framework import viewsets, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView 
from rest_framework.response import Response

from .serializers import  UsuarioSerializer, TareaSerializer, LoginSerializer
from .models import User, Tarea

# Create your views here.
 
class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
    
class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tareas to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    
        
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            print(user)
            token, created = Token.objects.get_or_create(user=user)
            print(token.key)
            contenido = {
                "token":token.key,
            }
            return Response(contenido ,status=status.HTTP_200_OK )

        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
            