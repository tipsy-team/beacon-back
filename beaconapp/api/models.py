from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='userprofile')
	phone = models.CharField(max_length=100, null=True, blank=True)


class Beacon(models.Model):
	unique_id = models.CharField(max_length=100, unique=True)
	name = models.CharField(max_length=100, null=True)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='beacons')
	description = models.TextField(null=True)

	def __str__(self):
		return self.unique_id

class LostBeacon(models.Model):
	beacon = models.ForeignKey(Beacon)
	active = models.BooleanField(default=True)
	date = models.DateTimeField()
	lat = models.CharField(max_length=30, null=True, blank=True)
	long = models.CharField(max_length=30, null=True, blank=True)
	description = models.TextField(null=True)


class FoundBeacon(models.Model):
	beacon = models.ForeignKey(Beacon)
	date = models.DateTimeField()
	lat = models.CharField(max_length=30, null=True, blank=True)
	long = models.CharField(max_length=30, null=True, blank=True)
	description = models.TextField(null=True)
	user = models.ForeignKey(User, null=True)
	distance = models.FloatField(null=True)
