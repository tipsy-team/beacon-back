from django.contrib import admin
from api.models import Beacon, FoundBeacon, LostBeacon
# Register your models here.



class BeaconAdmin(admin.ModelAdmin):
    list_display = ['unique_id','user','description']
    search_fields = ['user']

admin.site.register(Beacon, BeaconAdmin)


class LostBeaconAdmin(admin.ModelAdmin):
    list_display = ['beacon','date', 'lat', 'long', 'description']
    # search_fields = ['beacon__unique_id']

admin.site.register(LostBeacon, LostBeaconAdmin)


class FoundBeaconAdmin(admin.ModelAdmin):
    list_display = ['beacon','date', 'lat', 'long', 'description']
    # search_fields = ['beacon__unique_id']

admin.site.register(FoundBeacon, FoundBeaconAdmin)
