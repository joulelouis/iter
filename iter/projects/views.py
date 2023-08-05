# this 'render' method is going to allow us to render out the templates
from django.shortcuts import render

# Create your views here.
# views.py this is where the business logic will be taken care of for the functions that get triggered when the urls are activated

from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'My Portfolio Website',
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I\'m still working on',
    },
]

# in Django, views are python functions or classes that handle the logic for processing incoming HTTP requests and returning appropriate HTTP responses. Views are responsible for rendering templates, performing databse operations, and processing user input.
# this is an example of function-based views
def projects(request):
    # rendering data to templates
    page = 'projects'
    number = 12
    context = {'page': page, 'number': number, 'projects': projectsList}
            # render(request, 'template name', data to be rendered in dictionary type '{key: value}')
    return render(request, 'projects/projects.html', context)

# the added parameter pk is same as the URL endpoint <str:pk> where this view is called
def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-projects.html', {'project': projectObj})