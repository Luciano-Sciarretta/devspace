from django.db.models.signals import post_save
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models  import User



def create_profile(sender, instance, created, **kwargs):
    print("Antes de post_save")
    if created: 
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name= user.first_name
        )
        print("Signal post_save funcionando, perfil creado:", profile)
        
        
def delete_profile(sender, instance, **kwargs):
    try:
        user =instance.user
        user.delete()
    except User.DoesNotExist:
        pass

post_save.connect(create_profile, sender=User)
post_delete.connect(delete_profile, sender=Profile)
