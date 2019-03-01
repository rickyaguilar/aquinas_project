from django.shortcuts import render
from django.http import HttpResponse
from equipments.choices import price_choices, capacity_choices, location_choices

from equipments.models import Equipment
from consultants.models import Consultant

# Create your views here.
def index(request):
	equipments = Equipment.objects.order_by('-date_added').filter(is_published=True)[:3]

	context = {
		'equipments': equipments,
		'price_choices': price_choices,
		'capacity_choices': capacity_choices,
		'location_choices': location_choices
	}

	return render(request, 'pages/index.html', context)

def about(request):
	# Get all consultants
	consultants = Consultant.objects.order_by('-hire_date')

	# Get MVP
	mvp_consultant = Consultant.objects.all().filter(is_mvp=True)

	context = {
		'consultants': consultants,
		'mvp_consultant': mvp_consultant
	}

	return render(request, 'pages/about.html', context)
