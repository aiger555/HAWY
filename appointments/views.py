from rest_auth.registration.views import RegisterView
from .serializers import (
    PsychologistCustomRegistrationSerializer, PatientCustomRegistrationSerializer
    )


class PsychologistRegistrationView(RegisterView):
    serializer_class = PsychologistCustomRegistrationSerializer


class PatientRegistrationView(RegisterView):
    serializer_class = PatientCustomRegistrationSerializer
