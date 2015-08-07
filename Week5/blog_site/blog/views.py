from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from blog.models import Blog

# Create your views here.

def index(request):
	all_blogs = Blog.objects.all()

	return render(request,'blog/blog_index.html',{"blogs" : all_blogs})

def blog_id(request,num):
	tmp_blog = Blog.objects.get(pk=num)
	return render(request,'blog/blog.html',{"Title" : tmp_blog.title, "Text" : tmp_blog.text})

def create(request):
	if request.method == "GET":
		return render(request,'blog/create.html',{})

	new_blog = Blog()
	new_blog.title = request.POST["title"]
	new_blog.text = request.POST["text"]
	new_blog.save()

	return redirect('blog_id',new_blog.id)
