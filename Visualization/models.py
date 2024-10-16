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

class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    senior = models.TextField(blank=True, null=True)  
    junior = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def update_relationships(self, projects):
        senior_set = set()
        junior_set = set()
        
        for project in projects:
            contributors = [name.strip() for name in project.contributors.split(',') if name.strip()]
            mentors = [name.strip() for name in project.mentors.split(',') if name.strip()]

            if self.name in contributors:
                senior_set.update(mentors)
            if self.name in mentors:
                junior_set.update(contributors)

        self.senior = ', '.join(senior_set)
        self.junior = ', '.join(junior_set)
        self.save()

def populate_person_relationships():
    projects = FProject.objects.all()
    
    # Gather all unique names
    all_names = set()
    for project in projects:
        all_names.update([name.strip() for name in project.contributors.split(',') if name.strip()])
        all_names.update([name.strip() for name in project.mentors.split(',') if name.strip()])
    
    # Create or update Person instances
    for name in all_names:
        person, created = Person.objects.get_or_create(name=name)
        person.update_relationships(projects)