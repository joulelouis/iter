from django.forms import ModelForm
from .models import Project

#create a ProjectForm that will inherit from the ModelForm
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        #for the fields object, you can store a list ['field1', 'field2'] for the field in the model or if you want all the fields, use '__all__'
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']