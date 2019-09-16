from django.conf.urls import url
from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    url(r'^$', views.projects, name='projects'),
    path('<int:selected_project>/', views.project_details, name='project-details'),
    path('<int:selected_project>/edit/', views.edit_project_details, name='edit-project'),
]
