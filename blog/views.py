from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.all()
	context = {
		'title': 'Blog',
		'message': "Hola a todos!!",
		'posts': posts
	}
	return render(request, "post_list.html", context)

def post_create(request):

	form = PostForm(request.POST or None)

	context = {
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	else:
		print(form.is_valid())

	# if request.method == "POST":
	# 	title = request.POST.get("title").capitalize()
	# 	content = request.POST.get("content")
	# 	Post.objects.create(title=title, content=content)

	return render(request, "post_create.html", context)

def post_delete(request, id=None):
	
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Item Deleted")

	return redirect("posts:list")

	context = {
		'title': 'Borrar Post'
	}
	return render(request, "post_delete.html", context)

def post_update(request, id=None):
	
	instance = get_object_or_404(Post, id=id)

	form = PostForm(request.POST or None, instance=instance)

	if form.is_valid():
		
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, "Item Saved", extra_tags="some-else")

		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
		'title': 'Actualizar Post',
		'post': instance,
		'form': form
	}
	return render(request, "post_update.html", context)

def post_home(request):
	context = {
		'title': 'Home'
	}
	return render(request, "post_home.html", context)

def post_detail(request, id=None):
	
	context = {
		'title': 'Detalles'
	}

	if id:
		post = get_object_or_404(Post, id=id)
		context['post'] = post
	else:
		context['post'] = ""

	
	return render(request, "post_detail.html", context)
