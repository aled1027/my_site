from blog.models import *
from django.forms import ModelForm
from django import forms

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ["post"]

class PostForm(ModelForm):
	class Meta:
		model = Post

# class UploadFileForm(forms.Form):
	# f = forms.FileField()
	# name = forms.CharField(max_length=50)
