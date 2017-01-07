from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title", "content", "preview", "image"]
		widgets = {

			"title": forms.TextInput(attrs={'class' : 'input-field'}),
			"content": forms.Textarea(attrs={'class': 'materialize-textarea'}),
			"preview": forms.TextInput(attrs={'class' : 'input-field'}),
			"image" : forms.ClearableFileInput(attrs={'class': 'file-path validate', 'type' : 'text'})

		}

		labels = {
			"title": ("Titulo"),
			"content": ("Contenido"),
			"preview": ("Preview")
		}
