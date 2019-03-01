from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='equipments'),
	path('<int:equipment_id>', views.equipment, name='equipment'),
	path('search', views.search, name='search'),
]