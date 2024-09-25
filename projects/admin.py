from django.contrib import admin
from .models import Project 
from .models import Tag
from .models import Review



admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Review)


