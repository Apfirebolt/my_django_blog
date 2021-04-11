from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_blog import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('skills', TemplateView.as_view(template_name='skills.html'), name='skills'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('blogs/', include(('blogs.urls', 'blogs'), namespace='blogs')),
    path('projects/', include(('projects.urls', 'projects'), namespace='projects')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)