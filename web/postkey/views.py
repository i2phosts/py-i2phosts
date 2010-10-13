from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
from django.forms import ModelForm
from django.template import RequestContext

from web.postkey.models import i2phost
import re

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
		"""
		Here we do additional hostname validation as described in
		http://www.i2p2.i2p/naming.html
		"""
		data = self.cleaned_data['name']
		# convert hostname to lowercase
		data = data.lower()
		# Must end with '.i2p'.
		if re.match(r'.*\.i2p$', data) == None:
			raise forms.ValidationError('Hostname doesn\'t ends with .i2p')
		# Base 32 hostnames (*.b32.i2p) are not allowed
		if re.match(r'.*\.b32\.i2p$', data):
			 raise forms.ValidationError('Base 32 hostnames are not allowed')
		# Must contain only [a-z] [0-9] '.' and '-'
		h = re.match(r'([a-z0-9.-]+)\.i2p$', data)
		if h == None:
			raise forms.ValidationError('Illegal characters in hostname')
		else:
			namepart = h.groups()[0]
		# Must not contain '..'
		if re.search(r'\.\.', namepart):
			raise forms.ValidationError('".." in hostname')
		# Must not contain '.-' or '-.' (as of 0.6.1.33)
		if re.search(r'(\.-)|(-\.)', namepart):
			raise forms.ValidationError('Hostname contain ".-" or "-."')
		# Must not contain '--' except in 'xn--' for IDN
		if re.search(r'(?<!^xn)--', namepart):
			raise forms.ValidationError('Hostname contain "--" and it\'s not an IDN')
		# Certain hostnames reserved for project use are not allowed
		if re.search(r'(^|\.)(proxy|router|console)$', namepart):
			raise forms.ValidationError('Trying to use reserved hostname')
		return data
	def clean_b64hash(self):
		"""
		Base64 hash validation
		"""
		data = self.cleaned_data['b64hash']
		# Minimum key length 516 bytes
		if len(data) < 516:
			raise forms.ValidationError('Specified base64 hash are less than 516 bytes')
		# base64-i2p
		if re.match(r'[a-zA-Z0-9\-~]+AAAA$', data) == None:
			raise forms.ValidationError('Invalid base64 hash')
		# Avoid adding non-unique hashes
		qs = i2phost.objects.filter(b64hash=data)
		if qs.exists():
			raise forms.ValidationError('Base64 hash must be unique')
		return data

def addkey(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			form.save()
			request.session['hostname'] = form.cleaned_data['name']
			return HttpResponseRedirect('success')
	else:
		form = AddForm()
	return render_to_response('postkey.html', {
		'form': form,
		}, context_instance=RequestContext(request))

def success(request):
	return render_to_response('success_submission.html', {
		'hostname': request.session['hostname'],
		})
