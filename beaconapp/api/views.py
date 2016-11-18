from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import User

from permissions import IsAuthenticatedOrCreate
from serializers import SignUpSerializer, UserBeaconsSerializer, LostBeaconSerializer, CreateLostBeaconSerializer, CreateFoundBeaconSerializer, BeaconLocationsSerializer
from api.models import Beacon, LostBeacon, FoundBeacon

from rest_framework import generics, permissions, mixins
from rest_framework.response import Response


class SignUp(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = SignUpSerializer
	permission_classes = (IsAuthenticatedOrCreate,)


class UserBeacons(generics.ListCreateAPIView):
	queryset = Beacon.objects.all()
	serializer_class = UserBeaconsSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return Beacon.objects.filter(user=self.request.user)


class LostBeacons(generics.ListAPIView):
	queryset = LostBeacon.objects.all()
	serializer_class = LostBeaconSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return LostBeacon.objects.filter(active=True)


class CreateLostBeacon(generics.CreateAPIView):
	queryset = LostBeacon.objects.all()
	serializer_class = CreateLostBeaconSerializer
	permission_classes = [permissions.IsAuthenticated]


class CreateFoundBeacon(generics.CreateAPIView):
	queryset = FoundBeacon.objects.all()
	serializer_class = CreateFoundBeaconSerializer
	permission_classes = [permissions.IsAuthenticated]


class BeaconLocations(generics.ListAPIView):
	queryset = FoundBeacon.objects.all()
	serializer_class = BeaconLocationsSerializer
	permission_classes = [permissions.IsAuthenticated]
	lookup_field = 'beacon'

	def get(self, request, *args, **kwargs):
		if kwargs.get('beacon'):
			founds = FoundBeacon.objects.filter(beacon__user=request.user).filter(beacon__unique_id=kwargs.get('beacon'))
		else:
			founds = FoundBeacon.objects.filter(beacon__user=request.user)
		serializer = BeaconLocationsSerializer(founds, many=True)
		return Response(serializer.data)
