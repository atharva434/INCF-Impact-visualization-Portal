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
    # impact=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    def combined_fields(self):
        return f"{self.title}{self.description}{self.organization}{self.tech_stack}{self.domain}{self.subdomain}"

class Collab(models.Model):
    name=models.CharField(max_length=200)
    country=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Publication(models.Model):
    title=models.CharField(max_length=350)
    abstract=models.TextField(blank=True, null=True)
    domain=models.CharField(max_length=150)
    year=models.IntegerField()
    link=models.URLField(blank=True,null=True)

class FProject(models.Model):
    title=models.CharField(max_length=200)
    tags=models.CharField(max_length=200)
    status=models.CharField(max_length=100)
    contributors=models.CharField(max_length=100, blank=True, null=True)
    mentors=models.CharField(max_length=150, blank=True, null=True)
    about=models.TextField(blank=True, null=True)
    year=models.JSONField(default=True, blank=True)
    def combined_fields(self):
        return f"{self.title}{self.tags}{self.status}{self.contributors}{self.mentors}{self.about}"
