# any URL pattern that has anything to do with projects will be inside this url.py file

from django.urls import path
from . import views

urlpatterns =  [
    # path('endpoint', function-based view calling, URL name)
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),

    #create a URL pattern for the createProject view
    path('create-project/', views.createProject, name="create-project"),

    # create a URL pattern for the updateProject view that has an id as endpoint
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),

    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
]