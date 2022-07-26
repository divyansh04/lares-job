from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerialazer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"