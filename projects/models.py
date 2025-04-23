from django.db import models
from users.models import Profile
import uuid

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length= 200)
    description = models.TextField(null = True, blank = True)
    demo_link = models.CharField(max_length=2000, null = True, blank = True)
    source_link = models.CharField(max_length=2000, null = True, blank = True)
    featured_image = models.ImageField(null=True, blank=True, upload_to="projects/", default='projects/default.jpg')
    tags = models.ManyToManyField("Tag", blank = True)
    vote_total = models.IntegerField(default = 0, null = True)
    vote_ratio = models.IntegerField(default = 0, null = True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key= True, editable=False)
    
    class Meta:
        ordering = [ 'created']
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    VOTE_TYPE = (
        ("up", "Up Vote"),
        ("down", "Down Vote")
    )
    
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    body = models.TextField(null = True, blank = True)
    value = models.CharField(max_length= 200, choices = VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key= True, editable=False)
    
    def __str__(self):
        return self.value
   
   
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key= True, editable=False)
    
    def __str__(self):
        return self.name