from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
# Create your views here.

def index(request):
	benchmark_list = None
	template = loader.get_template('vericloud/index.html')
        context = RequestContext(request, {
                        'benchmark_list': benchmark_list,
                })

        return HttpResponse(template.render(context))



def detail(request, benchmark_user):
	return HttpResponse(benchmark_user)

def addMark(request):
	template = loader.get_template('vericloud/addMark.html')
	context = RequestContext(request, {
		'string': 'test'
		})
	return HttpResponse(template.render(context))