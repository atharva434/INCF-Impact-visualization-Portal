from django.contrib import admin
from .models import Organization,Project,Collab,Publication,FProject,Person
# Register your models here.

admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Collab)
admin.site.register(Publication)
admin.site.register(FProject)
admin.site.register(Person)