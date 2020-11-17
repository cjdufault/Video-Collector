from django import forms
from .models import Video

# form to add a Video
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'url', 'notes']
        

class SearchForm(forms.Form):
    search_term = forms.CharField()
        
