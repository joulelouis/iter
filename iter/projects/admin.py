from django.contrib import admin

# Register your models here.

#import the Project class from the models.py 
from .models import Project, Review, Tag

# this is to show the Project table in the Django admin
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
