from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.sessions.models import Session
from django.utils import timezone
from django_blog.settings import AUTH_USER_MODEL


class CustomUserManager(BaseUserManager):
  def create_superuser(self, email, password):
    user = self.model(email=email)
    user.set_password(password)
    user.is_superuser = True
    user.is_active = True
    user.is_staff = True
    user.save(using=self._db)
    return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField("Email", unique=True, max_length=255, blank=True, null=True)
  username = models.CharField("User Name", unique=True, max_length=255, blank=True, null=True)
  profile_image = models.FileField(upload_to='profile_image', blank=True, null=True)
  is_active = models.BooleanField('Active', default=True)
  is_staff = models.BooleanField('Staff', default=False)
  is_superuser = models.BooleanField('Super User', default=False)
  objects = CustomUserManager()
  USERNAME_FIELD = 'email'

  def remove_all_sessions(self):
    user_sessions = []
    all_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    for session in all_sessions:
      if str(self.pk) == session.get_decoded().get('_auth_user_id'):
        user_sessions.append(session.pk)
    return Session.objects.filter(pk__in=user_sessions).delete()

  def __str__(self):
    return self.email

  class Meta:
    '''Doc string for meta'''
    verbose_name_plural = "User"

