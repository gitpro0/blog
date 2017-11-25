from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import post
from .forms import post_form

def post_list(request):
	query = post.objects.all().order_by('-puplish')		#select * from post

	context = {
		'views_title' : 'list',
		'query' : query
	}

	return render(request, "list.html", context)

def post_create(request):
	form = post_form(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfuly Created')
		return HttpResponseRedirect(instance.get_url())

	context = {
		'views_title' : 'create',
		'btn' : 'Create',
		'form' : form
	}

	return render(request, "form.html", context)

def post_detail(request, id):

	instance = get_object_or_404(post,id=id)

	context = {
		'views_title' : 'detail',
		'instance' : instance
	}

	return render(request, "detail.html", context)

def post_update(request, id):
	instance = get_object_or_404(post, id=id)

	form = post_form(request.POST or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfuly Updated')
		return HttpResponseRedirect(instance.get_url())

	context = {
		'views_title' : 'update',
		'instance' : instance,
		'btn' : 'Edit',
		'form' : form
	}

	return render(request, "form.html", context)

def post_delete(request, id):
	instance = get_object_or_404(post, id=id)
	instance.delete()
	messages.success(request, 'Successfuly Deleted')
	return redirect('list')
