from django import forms
from django import forms
from blog.models import Post,Restaurant

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"    
        fields =["content"]

class Restaurant_Form(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"    