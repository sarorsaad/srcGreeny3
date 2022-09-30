from django.db import models

# Create your models here.
class Company(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="company/")
    subtitle = models.CharField(max_length=30)
    fb_link = models.URLField(null=True, blank=True)
    tw_link = models.URLField(null=True, blank=True)
    ins_link = models.URLField(null=True, blank=True)
    address = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=100)
    
    email = models.TextField(max_length=100)
    call_us = models.CharField(max_length=30)
    email_us = models.EmailField(max_length=30)
    
   
    
    

    def __str__(self):
        return str(self.name)