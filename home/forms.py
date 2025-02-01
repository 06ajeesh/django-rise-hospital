from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'
		widgets = {
			'p_name': forms.TextInput(
				attrs={'class': "form-control", 'id': "id_p_name", 'placeholder': "Name", 'required': 'required'}),
			'p_phone': forms.NumberInput(
				attrs={'class': "form-control", 'id': "id_p_phone", 'placeholder': "Phone", 'required': 'required'}),
			'p_email': forms.EmailInput(
				attrs={'class': "form-control", 'id': "id_p_email", 'placeholder': "Email", 'required': 'required'}),
			'doc_name': forms.Select(
				attrs={'class': "form-control", 'id': "id_doc_name", 'placeholder': "Doctor", 'required': 'required'}),
			'booking_date': forms.DateInput(
				attrs={'class': "form-control", 'id': "id_booking_date", 'type': "date", 'placeholder': "Date",
					   'required': 'required'}),
		}
		labels = {
			'p_name': "Patient Name",
			'p_phone': "Phone Number",
			'p_email': "Enter Email id",
			'doc_name': "Doctor Name",
			'booking_date': "Date of Booking",
		}