from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
# Create your views here.
def test(request):
	test = "jo"
	template = loader.get_template('userauth/password_change_form.html')
        context = RequestContext(request, {
                        'test': test,
                })

        return HttpResponse(template.render(context))
