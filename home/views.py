from django.shortcuts import render, redirect
from .models import Department, Doctors
from django.views import View
from .forms import BookingForm
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
	# return HttpResponse("<center><h2>Home Page</h2></center>")
	person = {'name': 'John', 'age': 25, 'place': "kochi"}
	return render(request, 'home.html', person)


def about(request):
	# return HttpResponse("<center><h2>About Page</h2></center>")
	return render(request, 'about.html')


class Booking(View):
	def get(self, request):
		return render(request, 'booking.html', {'form': BookingForm()})

	def post(self, request):
		form = BookingForm(request.POST)
		if form.is_valid():
			# Debugging output
			logger.debug(f"Form data: {form.cleaned_data}")

			# Save the form and check if it's actually being saved
			booking = form.save(commit=True)

			if booking:
				logger.debug(f"Booking saved with ID: {booking.id}")
			else:
				logger.error("Booking was not saved.")

			# After saving, redirect to the confirmation page
			return redirect('confirmation')
		else:
			# If form is not valid, output errors for debugging
			logger.error(f"Form errors: {form.errors}")
			return render(request, 'booking.html', {'form': form})


class ConfirmationView(View):
	def get(self, request):
		return render(request, 'confirmation.html')


def doctors(request):
	doc = Doctors.objects.all()
	return render(request, 'doctors.html', {"doctors": doc})


def contact(request):
	return render(request, 'contact.html')


def department(request):
	dep = Department.objects.all()
	return render(request, 'department.html', {"departments": dep})