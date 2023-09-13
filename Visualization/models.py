from django.db import models

# Create your models here.

class Organization(models.Model):
    name=models.CharField(max_length=100)
    aim=models.CharField(max_length=50,blank=True, null=True)
    use=models.TextField(blank=True,null=True)
    impact=models.TextField(blank=True,null=True)
    impact_json=models.JSONField(blank=True,null=True)
    url=models.URLField(blank=True,null=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True, null=True)
    organization=models.ForeignKey(Organization,on_delete=models.SET_NULL,null=True)
    tech_stack=models.CharField(max_length=100) #change max_length = 50
    domain=models.CharField(max_length=50,blank=True, null=True)
    subdomain=models.CharField(max_length=50,blank=True, null=True)
    # phone=models.IntegerField(max_length=10)
    impact=models.TextField(blank=True, null=True)


