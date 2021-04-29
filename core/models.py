from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone=models.CharField(max_length=14)
    image = models.FileField(upload_to='static/core/img')
    time = models.IntegerField(null=True)
    day = models.CharField(max_length=100, null=True)

class Patient(models.Model):
    gender = (
        ("MALE", "Male"),
        (" FEMALE", "Female"),
        ("CUSTOM", "Custom"),
    )
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=14)
    gender = models.CharField(max_length=20, choices=gender)

class Appointment(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=50,null=True)
    age=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    p_doctor=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=50,null=True)

class Prescription(models.Model):
    pname=models.CharField(max_length=30)
    date=models.DateField()
    bp=models.IntegerField()
    weight=models.IntegerField(null=True)
    medicine=models.TextField(max_length=30)
    additional_instruction=models.TextField(max_length=30)
    history=models.TextField(max_length=30)

class Feedback(models.Model):
    pname=models.CharField(max_length=30)
    feedback=models.TextField(max_length=40)

class Notification(models.Model):
    name=models.CharField(max_length=30)
    date=models.DateField()
    description=models.TextField(max_length=50)

class Medicine(models.Model):
    name=models.CharField(max_length=30)
    generic_name=models.CharField(max_length=30)








class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('user must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, default=None, null=True)
    last_name = models.CharField(max_length=255, default=None, null=True)
    email = models.EmailField(max_length=100, unique=True)

    username = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    session_token = models.CharField(max_length=10, default=0)

    is_active = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    phone = models.CharField(max_length=255, default=None, null=True )
    address = models.TextField()
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.FileField(upload_to='static/core/img')
    object = UserManager()







