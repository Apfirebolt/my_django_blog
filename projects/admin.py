from django.contrib import admin
from . models import Project, ProjectImages, ContactMessage


admin.site.register(Project)
admin.site.register(ProjectImages)
admin.site.register(ContactMessage)