from django.forms import ModelForm
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "featured_image", "demo_link", "source_link", "tags"]
        
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