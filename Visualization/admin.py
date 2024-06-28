from django.contrib import admin
from .models import Organization,Project,Collab,Publication
# Register your models here.

admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Collab)
admin.site.register(Publication)