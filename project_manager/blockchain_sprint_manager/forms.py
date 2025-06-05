from django import forms
from .models import Project, Sprint


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = '__all__'
