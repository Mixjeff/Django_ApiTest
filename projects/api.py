from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() ## Consulta todos los objetos
    permissions_classes = [permissions.AllowAny] ## Permisos para cualquiera
    serializer_class = ProjectSerializer