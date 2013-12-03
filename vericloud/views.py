from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from vericloud.models import Benchmark,  Testfile
import hashlib
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
	return HttpResponse(benchmark_user)

def newFile(request):
	return HttpResponse("lulz")


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

def listFiles(request):

	list = Testfile.objects.all()

	return render(request, 'vericloud/listFiles.html', {
		'list':list,
		})
	

def addFile(request):
	if(request.method == 'POST'):
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():

			#read file
			file = request.FILES['binary']
			data = file.read()
			file.seek(0)

			expResult = request.POST.get('expected_Result')

			hsh = hashlib.sha1()
			hsh.update(data)
			sha1 = hsh.hexdigest()

			#check if file already in database
			inDB = Testfile.objects.filter(sha1 = sha1)

			if inDB:
				form = FileForm();
				return render(request, 
					'vericloud/addFile.html', {
					'form' : form,
					'error': "sha1 bereits vorhanden"
				})

			newfile = Testfile(
				sha1 = sha1,
				filename = file,
				filesize = file.size, 
				binary= file,
				expected_result = expResult)
			newfile.save();


			return render(request, 'vericloud/fileDetail.html', {
				'file':file,
				'string':data,
				'expResult': expResult,
				'digest':sha1
			
		})	
		
		
			
		
	else:
		form = FileForm()

	return render(request, 'vericloud/addFile.html', {
		'form' : form
	})

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    
class FileForm (forms.Form):
	binary = forms.FileField(label='Select a file')
	expected_Result = forms.ChoiceField(
		choices = [('SAFE', 'SAFE'), ('UNSAFE', 'UNSAFE')], 
		widget=forms.RadioSelect())


