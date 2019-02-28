from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=   200)
    PhoneNumber= models.IntegerField(max_length=9)

    def __str__(self):
        return self.name