from rest_framework import serializers
from rest_framework.response import Response

from accounts.models import Doctor, Patient

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    pats = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    docs = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = ('__all__')
        depth = 1
