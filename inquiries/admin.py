from django.contrib import admin

from .models import Inquiry

class InquiryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'equipment', 'email', 'contact_date')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'email', 'equipment')
	list_per_page = 25


admin.site.register(Inquiry, InquiryAdmin)
