from django import forms
from diary.models import Memory


class diary_Form(forms.ModelForm):
    class Meta:
        model = Memory
        fields = "__all__"    