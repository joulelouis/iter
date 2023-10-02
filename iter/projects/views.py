# this 'render' method is going to allow us to render out the templates
from django.shortcuts import render, redirect


# Create your views here.
# views.py this is where the business logic will be taken care of for the functions that get triggered when the urls are activated
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


# in Django, views are python functions or classes that handle the logic for processing incoming HTTP requests and returning appropriate HTTP responses. Views are responsible for rendering templates, performing database operations, and processing user input.
# this is an example of function-based views
def projects(request):
    # rendering data to templates
    # all() -> retrieves all objects from the table 
    projects = Project.objects.all()
    context = { 'projects': projects }
            # render(request, 'template name', data to be rendered in dictionary type '{key: value}')
    return render(request, 'projects/projects.html', context)

# the added parameter pk is same as the URL endpoint <str:pk> where this view is called
def project(request, pk):
    # .get()-> retrieve a single object based on matched attribute (id=pk)
    projectObj = Project.objects.get(id=pk)
    
    return render(request, 'projects/single-projects.html', {'project': projectObj})

# create a createProject view for model form
def createProject(request):
    form = ProjectForm()

    # check if the method in the template is 'POST'
    if request.method == 'POST':
        # create a new instance of the ProjectForm
        # 'request.POST' is an attribute of the request object that contains a dictionary of data submitted via POST. Each form field's  name is a key, and the user's input is the corresponding value
        # 'request.FILES' attribute contains data form file input fields. It provides access to uploaded files as a dictionary. Each file input field's name in the HTML form becomes a key in the 'request.FILES' dictionary, and the corresponding value is a 'UploadedFile' object or a list of 'Uploaded file' objects if multiple files were selected for that field
        form = ProjectForm(request.POST, request.FILES)
        # is_valid() check if the form created by the user matched the requirements of the field parameters
        if form.is_valid():
            # .save() will save the created form by the user
            form.save()
            # redirect('urlpath name') will redirect the user to the url path, import the redirect module from the django.shortcuts
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

# updateProject view
# in this view, we need to pass a parameter 'pk' because we're going to update a specific project object
def updateProject(request, pk):
    # retrieve the specific Project object to be updated using its primary key (pk)
    project = Project.objects.get(id=pk)
    # Initialize a ProjectForm instance with data from the retrieved project. 'instance=project'its gonna prefill all the form fields with the project data 
    form = ProjectForm(instance=project)
  
    # Check if the HTTP request method is 'POST'
    if request.method == 'POST':
        # Initialize a new ProjectForm instance with data from the submitted POST request and the project instance
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # Check if the form is valid (passes validation checks)
        if form.is_valid():
            # Save the form data to update the project instance in the database
            form.save()
            # redirect to a specific URL (in this case, 'projects')
            return redirect('projects')

    # prepare the form and project data to be rendered in the template
    context = {'form': form}
    # render the 'projects/project_form.html' template with the form and project data
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    # query the project object
    project = Project.objects.get(id=pk)
    
    if request.method == 'POST':
        # .delete() method will delete the project object
        project.delete()
        return redirect('projects')
    
    # pass the queried object into the context dictionary
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)