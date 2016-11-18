from django.conf.urls import url, include
from django.contrib import admin
import oauth2_provider.views as oauth2_views
from django.conf import settings
from api import views
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    # OAuth 2 endpoints:
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
    url(r'^user/beacons$', views.UserBeacons.as_view(), name="user_beacons"),
    url(r'^lost_beacons$', views.LostBeacons.as_view(), name="lost_beacons"),
    url(r'^register_lost_beacon$', views.CreateLostBeacon.as_view(), name="register_lost_beacon"),
    url(r'^found_beacon$', views.CreateFoundBeacon.as_view(), name="found_beacon"),
    url(r'^beacon_locations/$', views.BeaconLocations.as_view(), name="beacons_locations"),
    url(r'^beacon_locations/(?P<beacon>.+)?$', views.BeaconLocations.as_view(), name="beacon_locations"),

]