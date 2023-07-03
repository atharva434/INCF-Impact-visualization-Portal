from django.db import models

# Create your models here.
<<<<<<< HEAD
=======

class Organization(models.Model):
    name=models.CharField(max_length=100)
    domain=models.CharField(max_length=50,blank=True, null=True)



class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True, null=True)
    organization=models.ForeignKey(Organization,on_delete=models.SET_NULL,null=True)
    tech_stack=models.CharField(max_length=100) #change max_length = 50
    domain=models.CharField(max_length=50,blank=True, null=True)
    subdomain=models.CharField(max_length=50,blank=True, null=True)
    # phone=models.IntegerField(max_length=10)
    impact=models.TextField(blank=True, null=True)


>>>>>>> 40b07e6c778106b005842f3c7be6dee0b9c34be1
