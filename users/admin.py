from django.contrib import admin
from .models import Profile
from .models import Skill, Message




admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)

