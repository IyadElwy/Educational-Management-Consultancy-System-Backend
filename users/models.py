from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)
    is_Student = models.BooleanField(default=False)
    is_Admin = models.BooleanField(default=False)
    is_Volunteer = models.BooleanField(default=False)
    is_School_Admin = models.BooleanField(default=False)
    username = models.EmailField(unique=True , null=False)

    USERNAME_FIELD = 'username'      #To avoid any clashing and renaming of a username field the username is also the email field

    REQUIRED_FIELDS = ['first_name','last_name','password']

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    #In Connecting Migration Add To School
    school = models.CharField(max_length=30, blank=True)



class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    profle_pic = models.ImageField(upload_to='profile_pic', blank=True)
    cv = models.FileField(upload_to='cv', blank=True, null=True)
    #In Connecting Migration Add To Wallet
class School_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    #In Connecting Migration Add To School

