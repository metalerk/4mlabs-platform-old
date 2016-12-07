from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm

prompt = "luis:~$ "

def post_list(request, deleted=False):
	posts = Post.objects.all().order_by("-timestamp")
	context = {
		'title': prompt + 'blog',
		'posts': posts
	}

	return render(request, "post_list.html", context)

def post_create(request):

	form = PostForm(request.POST or None)

	context = {
		"title": prompt + "create",
		"form": form,
	}

	if request.method == "POST":

		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "La entrada se ha creado correctamente.")
			return HttpResponseRedirect(instance.get_absolute_url())

		else:
			messages.error(request, "Error al crear el post")

	else:

		pass

	# if request.method == "POST":
	# 	title = request.POST.get("title").capitalize()
	# 	content = request.POST.get("content")
	# 	Post.objects.create(title=title, content=content)

	return render(request, "post_create.html", context)

def post_delete(request, id=None):
	
	instance = get_object_or_404(Post, id=id)
	instance.delete()

	return redirect("posts:list"	)

	context = {
		'title': prompt + 'delete'
	}
	return render(request, "post_delete.html", context)

def post_update(request, id=None):
	
	instance = get_object_or_404(Post, id=id)

	form = PostForm(request.POST or None, instance=instance)

	if request.method == "POST":

		if form.is_valid():
			
			instance = form.save(commit=False)
			instance.save()

			messages.success(request, "La entrada se ha actualizado correctamente.", extra_tags="success")

			return HttpResponseRedirect(instance.get_absolute_url())

		else:
			messages.error(request, "Error al actualizar", extra_tags="warning")

	else:

		pass


	context = {
		'title': prompt + "update",
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
	
	global prompt

	context = {}

	if id:
		post = get_object_or_404(Post, id=id)
		context['post'] = post
	else:
		context['post'] = ""

	context['title'] = prompt + post.title[:50]

	return render(request, "post_detail.html", context)
