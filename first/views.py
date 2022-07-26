from rest_framework import viewsets
from rest_framework import fields
from rest_framework.permissions import IsAuthenticated

from first import serializers
from django.contrib.auth import get_user_model

from .serializers import UserSerialazer

class UserViewset(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated)
    serializer_class = UserSerialazer
    queryset = get_user_model().objects.all()
