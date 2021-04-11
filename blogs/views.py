from django.views.generic import DetailView, ListView
from . models import Post


class ListPosts(ListView):
  """A View to list all the posts"""

  model = Post
  template_name = 'blogs/post-list.html'
  context_object_name = 'posts'

  def get_queryset(self):
    qs = Post.objects.all()
    return qs


class SinglePostDetail(DetailView):
  """A View to get single post"""

  model = Post
  context_object_name = 'post'
  template_name = 'blogs/post-detail.html'




