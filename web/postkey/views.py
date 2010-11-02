import re

from django import forms
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from web import settings
from web.postkey.models import i2phost
from web.lib.utils import get_logger
from web.lib.validation import validate_hostname
from web.lib.validation import validate_b64hash

class AddForm(ModelForm):
	"""
	This is our class for host-add form. It's based on django's ModelForm
	and uses our model "i2phost" (see postkey/models.py)
	"""
	class Meta:
		model = i2phost
		fields = ('name', 'b64hash', 'description')
		widgets = {
				'name': forms.TextInput(attrs={'size': '67'}),
				'b64hash': forms.Textarea(attrs={'rows': '1', 'cols': '100'}),
				'description': forms.Textarea(attrs={'rows': '2', 'cols': '72'})
				}
	def clean_name(self):
		"""Validate hostname"""
		data = self.cleaned_data['name']
		log.debug(u'hostname: %s', self.data['name'])
		data = validate_hostname(data)
		# Another set of reserved hostnames (suggested by zzz)
		if re.search(r'(^|\.)(i2p|i2p2|geti2p|mail|project|i2project|i2pproject|i2p-project).i2p$', data):
			raise forms.ValidationError('Trying to use hostname from additional reserved set')
		if data.count('.') > 1:
			raise forms.ValidationError('Currently only 2-level domains are allowed')
		return data
	def clean_b64hash(self):
		"""Validate base64 hash"""
		data = self.cleaned_data['b64hash']
		log.debug(u'hash: %s', self.data['b64hash'])
		data = validate_b64hash(data)
		return data

def addkey(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			log.debug('submit is valid, saving')
			form.save()
			request.session['hostname'] = form.cleaned_data['name']
			return HttpResponseRedirect('success')
	else:
		form = AddForm()
	return render_to_response('postkey.html', {
		'title': settings.SITE_NAME,
		'form': form,
		}, context_instance=RequestContext(request))

def success(request):
	return render_to_response('success_submission.html', {
		'title': settings.SITE_NAME,
		'hostname': request.session['hostname'],
		})

log = get_logger(filename=settings.LOG_FILE, log_level=settings.LOG_LEVEL)
