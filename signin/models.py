
from django.db import models

from operator import mod
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator, MinValueValidator

GENDER_CHOICE= (
    ('male','Male'),
    ('female','Female'),
    ('other','Other'),
)

MARITAL_CHOICE= (
    ('single', 'Single'),
    ('married', 'Married'),
    ('widowed', 'Widowed'),
    ('seperated', 'Seperated'),
    ('divorced', 'Divorced'),
    
)

FIRM_TYPE= (
    ('sole_proprietorship', 'Sole Proprietorship'),
    ('partnership', 'Partnership'),
    ('corporation', 'Corporation'),
    ('LLC', 'LLC'),
)

SECTOR= (
    ('healthcare', 'Healthcare'),
    ('finance', 'Finance'),
    ('automotive', 'Automotive'),
    ('telecommunications', 'Telecommunications'),
    ('food','Food'),
    ('construction', 'Construction'),
    ('manufacturing', 'Manufacturing'),
    ('mining','Mining'),
    ('energy', 'Energy'),
    ('chemical', 'Chemical'),
    ('aviation', 'Aviation'),
    ('information_Technology', 'Information Technology'),
    ('oil_&_gas', 'Oil & Gas'),
    ('public', 'Public'),
    ('others', 'Others'),

)


class User1(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    official_email=models.EmailField(max_length=50, unique=True)
    username=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField( validators=[ MinValueValidator(100000, 'Pin Code must have 6 digits') ])
    mobile= models.CharField(max_length=15)
    password= models.CharField(max_length=20, validators=[ MinLengthValidator(6,
     'password must have minimum of 6 characters') ]
            )
    date_of_birth=models.DateField()
    marital_status=models.CharField(max_length=10, choices=MARITAL_CHOICE, default='Single')
    gender=models.CharField(max_length=6, choices=GENDER_CHOICE, default='Male' )
    aadhar_no=models.CharField(max_length=14, validators=[ MinLengthValidator(12,
     'aadhar no must have 12 digits') ])
    business_name=models.CharField(max_length=100)
    type_of_firm=models.CharField(max_length=50, choices=FIRM_TYPE , default= "Corporation")
    sector=models.CharField(max_length=50, choices=SECTOR, default="Healthcare" )
    designation=models.CharField(max_length=50)
    office_address=models.CharField(max_length=250)
    GSTIN_No=models.CharField(max_length=16, validators=[ MinLengthValidator(10,
     'GSTIN No must have minimum 10 characters') ])
    total_staff=models.IntegerField()
    food_licence_no=models.PositiveBigIntegerField( validators=[ MinValueValidator(1000000000,
     'Food Licence No must have minimum 12 characters') ])
    official_website=models.CharField(max_length=100)
    


