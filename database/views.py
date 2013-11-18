from django.shortcuts import render
from django.http import HttpResponse
from database.models import Benchmark, Run
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
	