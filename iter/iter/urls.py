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
# import the settings.py file to connect our MEDIA_ROOT and MEDIA_URL
from django.conf import settings
# import static is basically going to help us create a URL for our static files
from django.conf.urls.static import static


# 'urlpatterns' is in charge of the URL routing system of the entire app. Each element in the list represents a URL pattern that will be mapped to a specific view
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('root domain', include('directory.fileName')) -> this will include all the url patterns in the url.py file
    # this is basically telling the program to "go to the directory/folder then go to the file"
    path('', include('projects.urls'))
]

# add a URL pattern to serve media files. This will serve the files uploaded by a user during development
# When a request is made to a URL that starts with the 'MEDIA_URL', Django will look for the requested file within the directory specified by 'MEDIA_ROOT'
# If the requested file exists in 'MEDIA_ROOT', Django will serve it as a response to the user's request
# This line of code allows you to serve user-uploaded media files during development, making them accessible through your web app
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)