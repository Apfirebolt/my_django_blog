from django.urls import path
from django.conf.urls.static import static
from django_blog import settings
from . views import ListPosts, SinglePostDetail


urlpatterns = [
    path('', ListPosts.as_view(), name='list'),
    path('<int:pk>', SinglePostDetail.as_view(), name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
