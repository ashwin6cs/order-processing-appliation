#models.py
from django.db import models
 
# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    item = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.firstname + " " + self.lastname
 
    class Meta:
        ordering = ['created']
         
    class Meta:  
        db_table = "blog_member"
        
class Member1(models.Model):
    
     
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    
    class Meta:  
        db_table = "info"