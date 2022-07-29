
from rest_framework import serializers
from django.forms import ValidationError
from django.contrib.auth.models import AbstractBaseUser
from signin.models import AbstractBaseUser, MyManager , User1
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import DjangoUnicodeDecodeError

class Emailserializer(serializers.ModelSerializer):
    email =serializers.EmailField()

    class Meta:
        model = User1
        fields=("email",)

class ResetPasswordSerializer(serializers.ModelSerializer):
    password= serializers.CharField(
        write_only=True,
        min_length=6
        )
    password2= serializers.CharField(
        write_only=True,
        min_length=6
    )

    class Meta:
        model = User1
        fields= ["password","password2",]

    def validate(self, data):
        try:
            password= data.get("password")
            password2= data.get("password2")
            token= self.context.get("kwargs").get("token")
            encoded_pk= self.context.get("kwargs").get("encoded_pk")

            if password != password2:
                raise serializers.ValidationError("password1 and password2 doesn't match")
        
            if token is None or encoded_pk is None:
                serializers.ValidationError("Missing Data")
            
            pk = urlsafe_base64_decode(encoded_pk).decode()
            user= User1.objects.get(pk=pk)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("The Reset Token Is Invalid")

            user.set_password(password)
            user.save()
            return data
            
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError("password1 and password2 doesn't match")