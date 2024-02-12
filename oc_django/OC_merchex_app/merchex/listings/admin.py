from django.contrib import admin

from listings.models import Band
from listings.models import Listing

# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band, BandAdmin)

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'band','sold', 'type')
admin.site.register(Listing, ListingsAdmin)