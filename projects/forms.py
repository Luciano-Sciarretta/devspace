from django import forms
from django.forms import ModelForm
from .models import Project, Review, Tag

class ProjectForm(ModelForm):

    tags = forms.CharField(required=False, widget= forms.Textarea(attrs={
        'placeholder': 'Add tags to your project (separated by commas)',
        'rows': '5',  
    }))
    
    def clean_tags(self):
        tags = self.cleaned_data['tags']
        return [tag.strip() for tag in tags.split(',') if tag.strip()]
    
    class Meta:
        model = Project
        fields = ["title", "description", "featured_image", "demo_link", "source_link"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form__input'})
            
            
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [ 'value', 'body']
        labels = {'value': 'Place your vote',
                  'body': 'Add a coment with your vote'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form__input'})