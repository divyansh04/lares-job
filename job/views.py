from multiprocessing import context
from django.urls import reverse_lazy
from rest_framework import generics, status, viewsets, response


from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from. import serializers


class PasswordReset(generics.GenericAPIView):

    serializer_class = serializers.EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)

     # localhost:8000/reset.password/<encoded_pk>/<token>/  

            reset_url = reverse(
             "reset-password",
              kwargs={"encoded_pk":encoded_pk,"token": token}
        
           )

            reset_url = f"localhost:8000{reset_url}"

            return response.Response(
             {
               "message":
               f"Your password reset link: {reset_url}"
             },
             status=status.HTTP_200_OK,
          )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
                )


class ResetPassword(generics.GenericAPIView):

   serializer_class = serializers.ResetPasswordSerailizer

   def patch(self, request, *args, **kwargs):
    
    serializer =self.serializer_class(
        data=request.data, context={"kwargs": kwargs}
    )

    serializer.is_valid(raise_exception=True)

    return response.Response(
        {"message": "Password reset complete"},
        status=status.HTTP_200_OK,
    )