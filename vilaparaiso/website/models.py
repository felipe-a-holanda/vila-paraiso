from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField('Name', max_length=200)
    email = models.CharField('Email', max_length=200, unique=True)
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
