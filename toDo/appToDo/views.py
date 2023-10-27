from django.contrib.auth import logout
from django.contrib.auth.models import User

from rest_framework import viewsets, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView 
from rest_framework.response import Response

from .serializers import  TareaSerializer
from .models import  Tarea

# Create your views here.    

class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tareas to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TareaSerializer
    def get_queryset(self):
        tareas =  Tarea.objects.filter(usuario=self.request.user)
        return tareas
    

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
