from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.template import RequestContext

from web.postkey.models import i2phost

class AddForm(ModelForm):
	class Meta:
		model = i2phost
		fields = ('name', 'b64hash')

def index(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/postkey/success/')
	else:
		form = AddForm()
	return render_to_response('postkey.html', {
		'form': form,
		}, context_instance=RequestContext(request))
