from django.db import models
import uuid 

# Create your models here.
# models.py - This is where we will create our database tables

class Project(models.Model):
    # create column field/attributes of the model
    # CharField() if for shorter text values
    # by default, the title will be a project object (UUID)
    title = models.CharField(max_length=200)
    # TextField() for longer text values
    # null=True means that this section is not required. If null is not set, by default it is 'False'
    # blank=True is for the Django to know that we are allowing to submit a form with the value being empty
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    # Tag model and Project model has ManyToMany relationship so ManyToManyField(modelName) is used
    # 'Tag' quotes is used since the Tag model is underneath the Project model. 
    tags = models.ManyToManyField('Tag', blank=True)
    # models.IntegerField() sets the value of the field to int
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    # DateTimeField() is like timestamps
    # auto_now_add=True sets the time automatically when the project/model is created
    created = models.DateTimeField(auto_now_add=True)
    # UUID means Universal Unique Identifier. UUIDs are 128-bit unique identifiers often used in database to ensure globally unique values, even across distributed systems.
    # default=uuid.uuid4 will automaticaly generate a random UUID as the 'id' value unless explicitly provided
    # unique=True means that each 'Project' object will have unique UUID as its primary key
    # primary_key=True designates the 'id' field as the primary key of the table.
    # editable=False prevents the 'id' field from being edited via forms in Django admin panel or other form interface
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # __str__(self) is a dunder method in Python
    # in this __str__, the value of the title given in the Project is the same as the given title by the superuser
    def __str__(self):
        return self.title

# create a Review class
class Review(models.Model):
    # VOTE_TYPE is an attribute from Review class that holds the choices for the value field/attribute
    # this is defined as a tuple of tuples
    VOTE_TYPE = (
        # ('actual value that gets stored in the database', 'display name for the choice')
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    # owner =
    # since Review model is a child of the Project model, this will be needing a ForeignKey()
    # on_delete=models.SET_NULL will set the Review of the project to null when the project is deleted. However, on_delete=models.CASCADE will set the Review of the project to be deleted when the project is deleted.
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    # choices=VOTE_TYPE sets the allowed choices to what is listed in the VOTE_TYPE field/attribute
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

# create a Tag model
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name