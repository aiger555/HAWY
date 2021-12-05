from rest_auth.registration.views import RegisterView
from rest_framework import viewsets

from .serializers import (
    DoctorCustomRegistrationSerializer, 
    PatientCustomRegistrationSerializer,
    DoctorSerializer,
    PatientSerializer,
    )

from .models import Doctor, Patient


class DoctorRegistrationView(RegisterView):
    serializer_class = DoctorCustomRegistrationSerializer


class PatientRegistrationView(RegisterView):
    serializer_class = PatientCustomRegistrationSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()