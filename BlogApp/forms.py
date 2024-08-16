from django import forms  
from BlogApp.models import Blog  
class BlogForm(forms.ModelForm):  
    class Meta:  
        model = Blog  
        fields = "__all__"