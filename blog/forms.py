from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title", "content", "preview"]
		widgets = {

			"title": forms.TextInput(attrs={'class' : 'input-field'}),
			"content": forms.Textarea(attrs={'class': 'materialize-textarea'}),
			"preview": forms.TextInput(attrs={'class' : 'input-field'})

		}

		labels = {
			"title": ("Titulo"),
			"content": ("Contenido"),
			"preview": ("Preview")
		}
