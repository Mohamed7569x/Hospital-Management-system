from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField()
    Gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='M')
    Phone = models.CharField(max_length=255, unique=True)
    Email = models.EmailField(max_length=255, unique=True)
    Address = models.CharField(max_length=255)
    Emergency_Contact = models.CharField(max_length=255)
    Medical_History = models.CharField(max_length=255)