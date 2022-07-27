from re import L
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
#import email
from rest_framework import fields, viewsets, serializers
from.models import User

from django.contrib.auth.models import User


MIN_LENGTH = 8


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only= True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"password must be longer than {MIN_LENGTH} characters."
        }
    )
    password2 = serializers.CharField(
        write_only= True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"password must be longer than {MIN_LENGTH} characters."
        }
    )


    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["password"] !=data["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            #password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            #address=validated_data["address"],
            pincode=validated_data["pincode"],
            state=validated_data["satate"],
            city=validated_data["city"],
            dob=validated_data["dob"],
            martialstatus=validated_data["martialstatus"],
            gender=validated_data["gender"],
            adharnum=validated_data["adharnum"],
            introduction=validated_data["introduction"],

            
        )

        user.set_password(validated_data["password"])
        user.save()

        return user



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer      