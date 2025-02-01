from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
				  path('', views.index, name='home'),
				  path('about/', views.about, name='about'),
				  path('booking/', views.Booking.as_view(), name='booking'),
				  path('doctors/', views.doctors, name='doctors'),
				  path('contact/', views.contact, name='contact'),
				  path('departments/', views.department, name='departments'),
				  path('confirmation/', views.ConfirmationView.as_view(), name='confirmation'),
			  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)