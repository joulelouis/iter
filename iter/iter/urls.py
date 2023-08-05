"""
URL configuration for iter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# imports the 'admin' module from Django's contrib package. The 'admin' module is used to handle Django's built-in admin interface, allowing you to manage your application's data models through a web interface.
from django.contrib import admin
# imports the 'path' function from the 'django.urls' modules. The 'path' function is a simple way to define URL patterns in Django
# import the 'include' function to connect the sub
from django.urls import path, include


# 'urlpatterns' is in charge of the URL routing system of the entire app. Each element in the list represents a URL pattern that will be mapped to a specific view
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('root domain', include('directory.fileName')) -> this will include all the url patterns in the url.py file
    # this is basically telling the program to "go to the directory/folder then go to the file"
    path('', include('projects.urls'))
]
