from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from vericloud.models import File, VerificationRun, VerificationResult, FileHierarchy, Requirement, Limitation
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


def createrun(request):
    limits = Limitation.objects.all()
    reqs = Requirement.objects.all()
    return render(request, 'vericloud/createrun.html', {
        'limits': limits,
        'reqs': reqs,
    })


def detail(request, benchmark_user):
    if benchmark_user == 'all':
        runs = VerificationRun.objects.all()
    else:
        runs = VerificationRun.objects.filter(user=benchmark_user)

    return render(request, 'vericloud/rundetail.html', {
        'runs': runs,
    })

    return HttpResponse(benchmark_user)


def newfile(request):
    return HttpResponse("lulz")


def addmark(request):
    if request.method == 'POST':
        return HttpResponse("LOL")
    else:
        form = ContactForm()

    return render(request, 'vericloud/addMark.html', {
        'form': form,
    })


def file(request, hashvalue):

    f = open('/home/leutheus/workspace/VerifierCloud/testfiles/' + hashvalue)

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

    result = FileHierarchy.objects.filter(parent=file_hierarchy_id)

    for fh in result:
        fh.file_id = File.objects.get(id=fh.file_id)

    return render(request, 'vericloud/file_hierarchies.html', {
        'file_hierarchies': result,
    })


def listreq(request):
    if request.method == 'POST':
        count = request.POST.get('count')
        mem = request.POST.get('mem')
        proctype = request.POST.get('cputype')

        #TODO validation!
        req = Requirement(processor_count=count, memory=mem, processor_type=proctype)
        try:
            req.save()
        except:
            pass
    requirements = Requirement.objects.all()
    return render(request, 'vericloud/requirements.html', {
        'requirements': requirements,
    })


def listlim(request):
    if request.method == 'POST':
        time = request.POST.get('time')
        mem = request.POST.get('mem')
        cpulim = request.POST.get('cpulimit')

        #TODO validation!
        lim = Limitation(time_limit=time, memory_limit=mem, processor_limit=cpulim)
        try:
            lim.save()
        except:
            pass
    limitations = Limitation.objects.all()
    return render(request, 'vericloud/limitations.html', {
        'limitations': limitations,
    })


def listfiles(request):

    filelist = File.objects.all()

    return render(request, 'vericloud/listFiles.html', {
        'list': filelist,

    })


def addfile(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():

            #read file
            file = request.FILES['binary']
            data = file.read()
            file.seek(0)

            expresult = request.POST.get('expected_Result')

            hsh = hashlib.sha1()
            hsh.update(data)
            sha1 = hsh.hexdigest()

            #check if file already in database

            return render(request, 'vericloud/fileDetail.html', {
                'file': file,
                'string': data,
                'expResult': expresult,
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


class RequirementForm(forms.Form):
    processor_count = forms.CharField()
    memory = forms.CharField()
