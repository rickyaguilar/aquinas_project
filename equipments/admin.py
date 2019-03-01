from django.contrib import admin

from .models import Equipment

# Register your models here.
class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('id','equipment_name','is_published','price','quantity','date_added',
	'consultant')
	list_display_links = ('id','equipment_name')
	list_filter = ('consultant',)
	list_editable = ('is_published',)
	search_fields = ('equipment_name','description','type','location')
	list_per_page = 25

admin.site.register(Equipment, EquipmentAdmin)