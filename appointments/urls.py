from django.urls import path

from .views import PsychologistRegistrationView, PatientRegistrationView


urlpatterns = [
    path('psychologists/', PsychologistRegistrationView.as_view(), name='psychologists'),
    path('patients/', PatientRegistrationView.as_view(), name='patients'),
]