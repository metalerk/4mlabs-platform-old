from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title", "content"]
		widgets = {

			"title": forms.TextInput(attrs={'placeholder': 'Titulo'}),
			"content": forms.Textarea(attrs={})

		}

		labels = {
			"title": ('Titulo'),
			"content": ("Contenido")
		}