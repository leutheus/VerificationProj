from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from database.models import Benchmark, Run
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def index (request):
	
	benchmark_list = Benchmark.objects.all();

	template = loader.get_template('database/index.html')
	context = RequestContext(request, {
			'benchmark_list': benchmark_list,
		})

	return HttpResponse(template.render(context))

def detail(request, benchmark_user):

	run_list = Run.objects.filter(benchmark__user__exact=benchmark_user);

	template = loader.get_template('database/detail.html')
	context = RequestContext(request, {
		'benchmark_user': benchmark_user,
		'run_list': run_list
		})
	return HttpResponse(template.render(context))
	
def search(request): 
	search = request.GET.get('name')
	return HttpResponseRedirect('/database/' + search)


def searchFile(request):
	searchFile = request.POST.get('filename')
	return HttpResponseRedirect('/database/searchFile/' + searchFile)

def file(request, file_name):

	template = loader.get_template('database/file.html')
	context = RequestContext(request, {
		'file_name': file_name
		})

	return HttpResponse(template.render(context))

def home(request):
	benchmark_list = Benchmark.objects.all();
	template = loader.get_template('database/home.html')
	context = RequestContext(request, {
		'benchmark_list': benchmark_list,
		})
	return HttpResponse(template.render(context))
