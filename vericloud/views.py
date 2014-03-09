from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from vericloud.models import File, VerificationRun, VerificationResult, FileHierarchy
from django.core.files import File as Filez
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


    runs = VerificationRun.objects.filter(user = benchmark_user)

    return render(request, 'vericloud/rundetail.html', {
        'runs' : runs,
    })


    return HttpResponse(benchmark_user)


def newFile(request):
    return HttpResponse("lulz")


def addMark(request):
    if (request.method == 'POST'):
        return HttpResponse("LOL")
    else:
        form = ContactForm()

    return render(request, 'vericloud/addMark.html', {
        'form': form,

    })


def file(request, hash):

    f = open('/home/leutheus/workspace/VerifierCloud/testfiles/' + hash)

    return render(request, 'vericloud/fileDetail.html', {
        'file': f.read(),
    })

def runresult(request, run_id):
    result = VerificationResult.objects.filter(run=run_id)
    if result.count() > 0:
        result = result[0]
    else:
        result = None
    return render(request, 'vericloud/runresult.html', {
        'result': result,
    })


def filehierarchy(request, file_hierarchy_id):
    print(file_hierarchy_id)
    result = FileHierarchy.objects.filter(parent=file_hierarchy_id)

    for fh in result:
        fh.file_id = File.objects.get(id=fh.file_id)

    return render(request, 'vericloud/file_hierarchies.html', {
        'file_hierarchies': result,
    })


def listFiles(request):

    list = File.objects.all()

    return render(request, 'vericloud/listFiles.html', {
        'list': list,

    })


def addFile(request):
    if request.method == 'POST':
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




            return render(request, 'vericloud/fileDetail.html', {
                'file': file,
                'string': data,
                'expResult': expResult,
                'digest': sha1

            })




    else:
        form = FileForm()

    return render(request, 'vericloud/addFile.html', {
        'form': form
    })


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)


class FileForm(forms.Form):
    binary = forms.FileField(label='Select a file')
    expected_Result = forms.ChoiceField(
        choices=[('SAFE', 'SAFE'), ('UNSAFE', 'UNSAFE')],
        widget=forms.RadioSelect())


