from django.shortcuts import render, redirect, HttpResponse
from .models import Course

# Create your views here.
def index(request):
	print(Course.objects.all())
	context = {
	'courses': Course.objects.all()
	#runs SELECT * FROM Course
	}
	return render(request, 'coursesApp/index.html', context)

def process(request):
	# course = Course.objects.get(id=id)
	c = Course.objects.create (name=request.POST['name'], description = request.POST['description'])
	c.save()
	#using ORM

	# Course.objects.create (name=request.POST['name'], description = request.POST['description'])

	#insert into course(name, description, created_at, updated_at) values (name, description, now(), now() )
	return redirect('/')

def remove(request, id):
	context={
		'remove': Course.objects.get(id=id),
	}
	return render(request, 'coursesApp/delete.html', context)

def delete(request, id):
	blah = Course.objects.get(id=id)
	if request.POST[u'response'] == "No":
		pass
	if request.POST[u'response'] == "Yes! I want to delete this":
		blah.delete()
	return redirect('/')






