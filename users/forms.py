from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
          
        self.fields['first_name'].widget.attrs.update({
            'class': 'form__input',
            'placeholder': 'Enter your name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form__input',
            'placeholder': 'Enter your email'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form__input',
            'placeholder': 'Choose a username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form__input',
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form__input',
            'placeholder': 'Confirm your password'
        })
        
        
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'location', 'email', 'short_intro', 'bio', 'profile_image', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website']
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            
            field.widget.attrs.update({'class': 'form__input'})
            
            
class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']
        
            
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field in self.fields.values():
                
                field.widget.attrs.update({'class': 'form__input'})
                
                
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form__input'})