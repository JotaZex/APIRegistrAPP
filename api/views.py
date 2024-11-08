from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .models import *

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer 