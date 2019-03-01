from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Rental

# Create your views here.
def rental(request):
	if request.method == "POST":
		equipment = request.POST['equipment']
		equipment_id = request.POST['equipment_id']
		name = request.POST['name']
		email = request.POST['email']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		status = request.POST['status']
		user_id = request.POST['user_id']

		if request.user.is_authenticated:
			user_id = request.user.id

		rental = Rental(equipment=equipment, equipment_id=equipment_id, name=name,
		email=email, start_date=start_date, end_date=end_date, status=status, user_id=user_id)

		rental.save()
		
		messages.success(request, 'Your request has been submitted, a consultant will get back to you soon.')
		return redirect('/equipments/'+equipment_id)