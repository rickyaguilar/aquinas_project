from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Inquiry

# Create your views here.
def inquiry(request):
	if request.method == 'POST':
		equipment_id = request.POST['equipment_id']
		equipment = request.POST['equipment']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		consultant_email = request.POST['consultant_email']

		# Check if user has made inquiry
		if request.user.is_authenticated:
			user_id = request.user.id
			# has_inquired = Inquiry.objects.all().filter(equipment_id=equipment_id, user_id=user_id)
			# if has_inquired:
			# 	messages.error(request, 'You have already made an inquiry for this listing')
			# 	return redirect('/equipments/'+equipment_id)

		inquiry = Inquiry(equipment=equipment, equipment_id=equipment_id, name=name, email=email,
		phone=phone, message=message, user_id=user_id)

		inquiry.save()

		send_mail(
			'Equipment Inquiry',
			'There has been an inquiry for ' + equipment + '. Our consultant will get back to you.',
			'rickyjamesaguilar@gmail.com',
			[consultant_email, 'rickyjamesaguilar@gmail.com'],
			fail_silently=False

		messages.success(request, 'Your inquiry has been submitted, a consultant will get back to you soon.')
		return redirect('/equipments/'+equipment_id)
