from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=225, blank=True, null=True)
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.get_full_name()
    
    def get_username(self):
        return self.email
    

class Products(models.Model):
    name = models.CharField(max_length=225)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    image = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name