from pyi2phosts.postkey.models import i2phost
from pyi2phosts.postkey.models import PendingHost
from django.contrib import admin

class i2phostAdmin(admin.ModelAdmin):
	def url(self, hostname):
		return '<a href=http://' + hostname.name + '>look</a>'
	url.allow_tags = True

	list_display = ('url', 'name', 'description', 'date_added', 'last_seen', 'expires',
			'activated', 'external')
	list_display_links = ['name']
	list_filter = ('activated', 'external', 'approved')
	search_fields = ['name']
	ordering = ['date_added']

class PendingAdmin(i2phostAdmin):
	def queryset(self, request):
		qs = super(PendingAdmin, self).queryset(request)
		return qs.filter(approved=False)

	list_filter = []
	list_display = ('url', 'name', 'description', 'date_added', 'last_seen', 'expires', 'approved')
	list_editable = ['approved']

admin.site.register(i2phost, i2phostAdmin)
admin.site.register(PendingHost, PendingAdmin)
