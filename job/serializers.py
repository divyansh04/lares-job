from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode

class EmailSerializer(serializers.Serializer):
    
    email = serializers.EmailField()


    class Meta:
        fields = ("email",)


class ResetPasswordSerailizer(serializers.Serializer):
    password = serializers.CharField(
    write_only=True,
    min_length=4,   
    )
    class Meta:
        fields = ("password",)

    def validate(self, data):
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            serializers.ValidationError("Missing data")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data