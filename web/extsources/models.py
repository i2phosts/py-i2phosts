from django.db import models

from lib.validation import validate_i2purl

class ExternalSource(models.Model):
	name = models.CharField(max_length=128, unique=True)
	url = models.CharField(max_length=256, validators=[validate_i2purl])
	description = models.CharField(max_length=512, blank=True)
	last_modified = models.DateTimeField(null=True, blank=True)
	last_success = models.DateTimeField(null=True, blank=True)
	etag = models.CharField(max_length=256, blank=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

