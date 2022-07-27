from secrets import choice

from . models import User1
from rest_framework import fields, viewsets, serializers, status, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator




class UserSerializer(serializers.ModelSerializer):
    

    password = serializers.CharField ( write_only= True,
        validators=[ MinLengthValidator(6, 'password must have 6 characters') ]
        )

    password2 = serializers.CharField( write_only= True,
        validators=[ MinLengthValidator(6, 'password must have 6 characters') ]
         )


    class Meta:
        model= User1
        fields= "__all__"
        
    def validate(self, data):

        if User1.objects.filter(official_email=data['official_email']).exists():
            raise serializers.ValidationError(
                {'official_email', ('Email Already Exists')} )
        
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords doesnot match eachother.")
        return data

    def create(self, validated_data):
        signin= User1.objects.create (

            username=validated_data['username'],
            official_email=validated_data['official_email'],
            password=validated_data['password'],
            
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            mobile=validated_data['mobile'],
            state=validated_data['state'],
            city=validated_data['city'],
            pincode=validated_data['pincode'],
            date_of_birth=validated_data['date_of_birth'],
            marital_status=validated_data['marital_status'],
            gender=validated_data['gender'],
            aadhar_no=validated_data['aadhar_no'],
            business_name=validated_data['business_name'],
            type_of_firm=validated_data['type_of_firm'],
            sector=validated_data['sector'],
            designation=validated_data['designation'],
            office_address=validated_data['office_address'],
            GSTIN_No=validated_data['GSTIN_No'],
            total_staff=validated_data['total_staff'],
            food_licence_no=validated_data['food_licence_no'],
            official_website=validated_data['official_website'],
            
        )

        signin.save()

        return signin

class UserViewSet(viewsets.ModelViewSet):
    queryset= User1.objects.all()
    serializer_class = UserSerializer


