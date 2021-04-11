from django.views.generic import DetailView, ListView
from . models import Project


class ListProjects(ListView):
  """A View to list all the projects"""

  model = Project
  template_name = 'projects/project-list.html'
  context_object_name = 'projects'

  def get_queryset(self):
    qs = Project.objects.all()
    return qs


class SingleProjectDetail(DetailView):
  """A View to get single project"""

  model = Project
  context_object_name = 'project'
  template_name = 'projects/project-detail.html'




