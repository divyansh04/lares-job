
from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager
from operator import mod

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





class MyManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Must provide email")
        if not username:
            raise ValueError("Must provide username")

        user =self.model(
            email= self.normalize_email(email),
             username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user =self.create_user(
            email= self.normalize_email(email),
            password=password,
             username=username,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user





class User1( AbstractBaseUser):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50, unique=True)
    username=models.CharField(max_length=100, unique=True)
    address=models.CharField(max_length=255)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10, validators=[ MinLengthValidator(6, 'Pin Code must have 6 digits') ])
    mobile= models.CharField(max_length=15 ,unique=True)
    password= models.CharField(max_length=255, validators=[ MinLengthValidator(6,
     'password must have minimum of 6 characters') ]
            )
    date_of_birth=models.DateField(null=True)
    marital_status=models.CharField(max_length=10, choices=MARITAL_CHOICE, default='Single')
    gender=models.CharField(max_length=6, choices=GENDER_CHOICE, default='Male' )
    aadhar_no=models.CharField(max_length=14, unique=True, null= True, validators=[ MinLengthValidator(12,
     'aadhar no must have 12 digits') ])
    business_name=models.CharField(max_length=100)
    type_of_firm=models.CharField(max_length=50, choices=FIRM_TYPE , default= "Corporation")
    sector=models.CharField(max_length=50, choices=SECTOR, default="Healthcare" )
    designation=models.CharField(max_length=50)
    office_address=models.CharField(max_length=250)
    GSTIN_No=models.CharField(max_length=16, validators=[ MinLengthValidator(10,
     'GSTIN No must have minimum 10 characters') ])
    total_staff=models.IntegerField(null=True)
    food_licence_no=models.CharField(max_length=20, null=True, validators=[ MinLengthValidator(12,
     'Food Licence No must have minimum 12 digits') ])
    official_website=models.CharField(max_length=100)
    is_staff = True #models.BooleanField( default=False)
    is_active = True #models.BooleanField( default=True)
    is_superuser = False #models.BooleanField( default=False)
    is_admin = True #models.BooleanField( default=False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyManager()

    def __str__ (self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    


