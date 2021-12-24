from rest_framework import serializers

from .models import Appointment

from accounts.models import User
from accounts.serializers import UserSerializer


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('__all__')
        depth = 1

        