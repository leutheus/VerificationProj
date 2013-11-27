from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from vericloud.models import Benchmark,  Testfile
# Create your views here.

from django import forms

def index(request):
	benchmark_list = None
	template = loader.get_template('vericloud/index.html')
        context = RequestContext(request, {
                        'benchmark_list': benchmark_list,
                })

        return HttpResponse(template.render(context))



def detail(request, benchmark_user):
	return HttpResponse("verhext")




def addMark(request):

	if (request.method == 'POST'):
		return HttpResponse("LOL")
	else:
		form = ContactForm()
		run_list = Testfile.objects.all()
	return render(request, 'vericloud/addMark.html', {
        'form': form,
        'run_list' : run_list,
    })
	
def addFile(request):
	if(request.method == 'POST'):
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES['binary']
			
			return HttpResponse("Add to Database lul ")
		
		
	else:
		form = FileForm()

	return render(request, 'vericloud/addFile.html', {
		'form' : form
	})

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    
class FileForm (forms.Form):
	binary = forms.FileField(label='Select a file')


