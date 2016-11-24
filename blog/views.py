from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post

def post_list(request):
	posts = Post.objects.all()
	context = {
		'title': 'Blog',
		'message': "Hola a todos!!",
		'posts': posts
	}
	return render(request, "post_list.html", context)

def post_create(request):
	context = {
		'title': 'Crear Post'
	}
	return render(request, "post_create.html", context)

def post_delete(request):
	context = {
		'title': 'Borrar Post'
	}
	return render(request, "post_delete.html", context)

def post_update(request):
	context = {
		'title': 'Actualizar Post'
	}
	return render(request, "post_update.html", context)

def post_home(request):
	context = {
		'title': 'Home'
	}
	return render(request, "post_home.html", context)

def post_detail(request, id=None):
	
	context = {
		'title': 'Detalles',
	}

	if id:
		post = get_object_or_404(Post, id=id)
		context['post'] = post
	else:
		context['post'] = ""

	
	return render(request, "post_detail.html", context)
