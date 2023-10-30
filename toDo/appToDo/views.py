from django.contrib.auth import logout

from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView 
from rest_framework.response import Response

from .serializers import  TareaSerializer
from .models import  Tarea


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

# Create your views here.    

class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tareas to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = TareaSerializer
    def get_queryset(self):
        tareas =  Tarea.objects.filter(usuario=self.request.user)
        return tareas

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.save()

    refresh = RefreshToken.for_user(user)
    data = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

    return Response(data, status=status.HTTP_201_CREATED)    


@api_view(['POST'])
@permission_classes([AllowAny])
def custom_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(password):
        return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    data = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'usuario_id': user.id,
    }

    return Response(data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class veryToken(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        return Response(status=status.HTTP_200_OK)