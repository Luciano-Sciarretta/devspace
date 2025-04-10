from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

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