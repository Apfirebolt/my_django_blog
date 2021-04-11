from django.db import models
from django_blog.settings import AUTH_USER_MODEL

class Project(models.Model):
  title = models.CharField('Project Title', max_length=200)
  content = models.CharField('Project Content', max_length=500)
  created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects_created')
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  is_deleted = models.BooleanField(default=False)

  def __str__(self):
    return 'Project (%s, %s)' % (self.created_by.username, self.title)

  class Meta:
    verbose_name_plural = "Projects"


class ProjectImages(models.Model):
  title = models.CharField("Image Title", max_length=140, blank=True, null=True)
  description = models.CharField("Image Description", max_length=250, blank=True, null=True)   
  related_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='all_project_images')
  image = models.ImageField(upload_to='project_images')

  def __str__(self):
    return str(self.related_project.title) + ' - ' + str(self.description)

  class Meta:
    verbose_name_plural = "Project Images"


class ContactMessage(models.Model):
  name = models.CharField("Name", max_length=100)
  email = models.CharField("Email", max_length=250)
  message = models.CharField("Message", max_length=250)    

  def __str__(self):
    return str(self.name) + ' - ' + str(self.email)

  class Meta:
    verbose_name_plural = "Contact Messages"



