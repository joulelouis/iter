# any URL pattern that has anything to do with projects will be inside this url.py file

from django.urls import path
from . import views

urlpatterns =  [
    # path('endpoint', function-based view calling, URL name)
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
]