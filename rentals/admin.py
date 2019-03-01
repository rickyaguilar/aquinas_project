from django.contrib import admin

from .models import Rental

class RentalAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'equipment', 'email', 'contact_date', 'start_date', 'end_date')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'email', 'equipment')
	list_per_page = 25


admin.site.register(Rental, RentalAdmin)
