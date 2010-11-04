from django.contrib import admin

from pyi2phosts.extsources.models import ExternalSource


class ExternalSourceAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'description', 'last_success', 'last_modified', 'etag', 'active')
	list_editable = ['active']

admin.site.register(ExternalSource, ExternalSourceAdmin)
