from rest_framework import serializers

from .models import Appointment, PastAppointment


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('__all__')
        depth = 1
    

class PastAppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PastAppointment
        fields = ('__all__')
        depth = 1