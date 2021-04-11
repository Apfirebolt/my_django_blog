from django.db import models
from django_blog.settings import AUTH_USER_MODEL

class Post(models.Model):
  title = models.CharField('Post Title', max_length=200)
  content = models.CharField('Post Content', max_length=500)
  created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_created')
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  is_published = models.BooleanField(default=False)
  is_deleted = models.BooleanField(default=False)

  def __str__(self):
    return 'Post (%s, %s)' % (self.created_by.username, self.title)

  class Meta:
    verbose_name_plural = "Posts"


class PostImages(models.Model):
  title = models.CharField("Image Title", max_length=140, blank=True, null=True)
  description = models.CharField("Image Description", max_length=250, blank=True, null=True)   
  related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='all_post_images')
  image = models.ImageField(upload_to='post_images')

  def __str__(self):
    return str(self.related_post.title) + ' - ' + str(self.description)

  class Meta:
    verbose_name_plural = "Post Images"


class Tags(models.Model):
  name = models.CharField(max_length=140)  
  created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tags_created')
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.name)

  class Meta:
    verbose_name_plural = "Tags"


