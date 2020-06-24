from rest_framework import (
     views, viewsets, )
from backend.models import *
from .serializers import * 
class UserDetail(viewsets.ModelViewSet):
    """
    api for the user registration
    """
    model = Backend
    serializer_class = BackendSerializer
    queryset = Backend.objects.all()

