from school.models import *
from django.forms import ModelForm
from django import forms

class HomeworkForm(ModelForm):
	class Meta:
		model = Homework

class CourseForm(ModelForm):
	class Meta:
		model = Course
class ProgramForm(ModelForm):
	class Meta:
		model = Program
		exclude=['created']

# class UploadFileForm(forms.Form):
    # f = forms.FileField()
    # name = forms.CharField(max_length=50)
