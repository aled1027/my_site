from blog.models import *
from django.forms import ModelForm

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ["post"]

class PostForm(ModelForm):
	class Meta:
		model = Post
