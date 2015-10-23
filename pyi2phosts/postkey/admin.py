from django.contrib import admin
from django import forms

from pyi2phosts.lib.utils import get_b32
from pyi2phosts.postkey.models import i2phost
from pyi2phosts.postkey.models import PendingHost
from pyi2phosts.lib.validation import validate_hostname
from pyi2phosts.lib.validation import validate_b64hash


class i2phostAdminForm(forms.ModelForm):
	""" Custom form for editing hosts via admin interface """

	def clean_name(self):
		"""Validate hostname"""
		data = self.cleaned_data['name']
		data = validate_hostname(data)
		return data

	def clean_b64hash(self):
		"""Validate base64 hash"""
		data = self.cleaned_data['b64hash']
		data = validate_b64hash(data, check_uniq=False)
		return data


class i2phostAdmin(admin.ModelAdmin):
	def url(self, hostname):
		return '<a href="http://' + get_b32(hostname.b64hash) + '">b32</a>'

	form = i2phostAdminForm
	url.allow_tags = True
	list_display = ('url', 'name', 'description', 'date_added', 'last_seen', 'expires',
			'activated', 'external')
	list_display_links = ['name']
	list_filter = ('activated', 'external', 'approved')
	search_fields = ('name', 'b64hash')
	ordering = ['-date_added']


class PendingAdmin(i2phostAdmin):
	def queryset(self, request):
		qs = super(PendingAdmin, self).queryset(request)
		return qs.filter(approved=False)

	def approve_selected(modeladmin, request, queryset):
		queryset.update(approved=True)

	list_filter = []
	list_display = ('url', 'name', 'description', 'date_added', 'last_seen', 'expires', 'approved')
	actions = ['approve_selected']


admin.site.register(i2phost, i2phostAdmin)
admin.site.register(PendingHost, PendingAdmin)
