from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null= True, blank=True)
    name = models.CharField(max_length= 200, blank= True, null=True)
    username = models.CharField(max_length=200, null=True, blank = True)
    location = models.CharField(max_length=200, null=True, blank = True)
    email = models.EmailField(max_length= 500, null = True, blank = True)
    short_intro = models.CharField(max_length=200, null=True, blank = True)
    bio = models.TextField( null=True, blank = True)
    profile_image = models.ImageField( null=True, blank = True, upload_to='profiles/', default= 'profiles/user-default.png')
    
    social_github = models.CharField(max_length= 200, blank= True, null=True)
    social_twitter = models.CharField(max_length= 200, blank= True, null=True)
    social_linkedin = models.CharField(max_length= 200, blank= True, null=True)
    social_youtube = models.CharField(max_length= 200, blank= True, null=True)
    social_website = models.CharField(max_length= 200, blank= True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key= True, editable=False)
    
    def __str__(self):
        return str(self.username) or self.name or "Unnamed Profile"
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile,  null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key= True, editable=False)
    
    def __str__(self):
        return self.name if self.name else "Without name"
    
    
    
class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_messages')
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='received_messages')
    subject = models.CharField(max_length=200)
    body = models.TextField()
    #No uso el name y mail del modelo  Profile por si un usuario sin cuenta quiere enviar mensajes
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    is_read = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key= True, editable=False)
    
    
    
    def __str__(self):
        return self.subject or 'Without subject'
    
    class Meta:
        ordering = ['is_read', '-created']
        indexes = [
        models.Index(fields=['sender', 'created']),
        models.Index(fields=['recipient', 'is_read', 'created']),
    ]