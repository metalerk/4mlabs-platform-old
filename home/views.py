from django.shortcuts import render
from blog.models import Post

def home(request):
	blog = "posts/"
	create_post = blog + "create"
	ip_addr = request.META['REMOTE_ADDR']
	user_agent = request.META['HTTP_USER_AGENT']
	context = {
		"title": "#! /usr/bin/metalerk --home",
		"blog": blog,
		"create_post": create_post,
		"remote_ip" : ip_addr,
		"user_agent" : user_agent
	}
	return render(request, "index.html", context)