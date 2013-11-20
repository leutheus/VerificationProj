from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from database.models import Benchmark, Run, Testfile, Configuration
from django.template import RequestContext, loader

# Create your views here.

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
	
	file2 = Testfile.objects.filter(filename=file_name)
	for fi in file2:
		text = open(fi.binary.path)
		text = text.read()
	config = Configuration.objects.all()
	template = loader.get_template('database/file.html')
	context = RequestContext(request, {
		'file_name': file_name,
		'file': file2,
		'config': config,
		'text': text,
		})

	return HttpResponse(template.render(context))

def home(request):
	return HttpResponse("Hallo")