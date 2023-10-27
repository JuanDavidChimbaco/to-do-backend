"""
URL configuration for toDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from appToDo import views

router = DefaultRouter()
router.register(r'Tareas',views.TareaViewSet, basename='Tarea')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include (router.urls)),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('logout/', views.LogoutView.as_view())
]

# http://localhost:8000/api/Tareas/ es para obtener todas las tareas
# http://localhost:8000/api/Tareas/1/ es para obtener la tarea con id 1
# http://localhost:8000/api/token/ es para obtener el token : de acceess y refresh 
# http://localhost:8000/api/token/refresh/ es para obtener un nuevo token de acceso para extender su vida util