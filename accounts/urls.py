from django.urls import path

from .views import (
                    DoctorRegistrationView, 
                    PatientRegistrationView,
                    DoctorViewSet,
                    PatientViewSet,
                    )


urlpatterns = [
    path('registration/doctor/', DoctorRegistrationView.as_view(), name='register-doctor'),
    path('registration/patient/', PatientRegistrationView.as_view(), name='register-patient'),
    path('doctors/', DoctorViewSet.as_view({'get': 'list'})),
    path('patients/', PatientViewSet.as_view({'get': 'list'})),
    
]