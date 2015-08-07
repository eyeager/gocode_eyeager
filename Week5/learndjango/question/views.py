from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from models import Question

'''
def index(request):
	q = Question()
	q.title = "New"
	q.text = "another new"
	q.save()
	return render(request,'question/index.html',{})
'''

def index(request):
	names = ["Zoe","Bobby","Buddy"]
	return render(request,'question/index.html',{"Name" : names})

def blah(request):
	return HttpResponse("I am blah about Django")

def create(request):
	if request.method == "GET":
		return render(request,'question/create.html',{})

	q = Question()
	q.title = request.POST["title"]
	q.text = request.POST["text"]
	q.save()

	return redirect('lookup',q.id)

def lookup(request,num):
	q = Question.objects.get(pk=num)
	return HttpResponse("I'm the lookup: " + q.title)