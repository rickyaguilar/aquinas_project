from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, capacity_choices, location_choices

from .models import Equipment

# Create your views here.
def index(request):
	equipments = Equipment.objects.order_by('-date_added').filter(is_published=True)

	paginator = Paginator(equipments, 6)
	page = request.GET.get('page')
	paged_equipments = paginator.get_page(page)

	context = {
		'equipments': paged_equipments
	}

	return render(request, 'equipments/equipments.html', context)

def equipment(request, equipment_id):
	equipment = get_object_or_404(Equipment, pk=equipment_id)

	context = {
		'equipment': equipment
	}

	return render(request, 'equipments/equipment.html', context)

def search(request):
	queryset_list = Equipment.objects.order_by('-date_added')

	# Keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)

	# City
	if 'equipment_type' in request.GET:
		equipment_type = request.GET['equipment_type']
		if equipment_type:
			queryset_list = queryset_list.filter(equipment_type__icontains=equipment_type)

	# State
	if 'location' in request.GET:
		location = request.GET['location']
		if location:
			queryset_list = queryset_list.filter(location__iexact=location)

	# Bedrooms
	if 'capacity' in request.GET:
		capacity = request.GET['capacity']
		if capacity:
			queryset_list = queryset_list.filter(capacity__lte=capacity)

	# Price
	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__lte=price)

	context = {
		'price_choices': price_choices,
		'capacity_choices': capacity_choices,
		'location_choices': location_choices,
		'equipments': queryset_list,
		'values': request.GET
	}
	return render(request, 'equipments/search.html', context)