from django.shortcuts import render
from blog.models import Post

def home(request):
	blog = "posts/"
	create_post = blog + "create"
	context = {
		"title": "#! /usr/bin/metalerk --home",
		"blog": blog,
		"create_post": create_post
	}
	return render(request, "index.html", context)