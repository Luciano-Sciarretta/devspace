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
        ordering = [ '-vote_ratio', '-vote_total', 'title']
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner_id', flat = True)
        return queryset

    @property
    def get_vote_count(self ):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value = 'up').count()
        totalVotes = reviews.count()
        ratio = ((upVotes * 100) / totalVotes)
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()
        
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    VOTE_TYPE = (
        ("up", "Up Vote"),
        ("down", "Down Vote")
    )
    
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    body = models.TextField(null = True, blank = True)
    value = models.CharField(max_length= 200, choices = VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key= True, editable=False)
    
    def __str__(self):
        return self.value
    class Meta:
       unique_together = [['owner', 'project']] # Mismo usuario puede hacer solamente una review de un proyecto
    
        
   
   
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key= True, editable=False)
    
    def __str__(self):
        return self.name