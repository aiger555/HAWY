from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from .models import Doctor, Patient, User


class DoctorCustomRegistrationSerializer(RegisterSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True)
    age = serializers.IntegerField(required=False)
    sertificate = serializers.CharField(required=True)
    experience = serializers.CharField(required=True)

    def get_cleaned_data(self):
            data = super(DoctorCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'age' : self.validated_data.get('age', ''),
                'sertificate' : self.validated_data.get('sertificate', ''),
                'experience': self.validated_data.get('experience', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(DoctorCustomRegistrationSerializer, self).save(request)
        user.is_doctor = True
        user.save()
        doctor = Doctor(
                        doctor=user, 
                        age=self.cleaned_data.get('age'), 
                        sertificate=self.cleaned_data.get('sertificate'),
                        experience=self.cleaned_data.get('experience')
                        )
        doctor.save()
        return user


class PatientCustomRegistrationSerializer(RegisterSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True,) 
    
    def get_cleaned_data(self):
            data = super(PatientCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'age' : self.validated_data.get('age', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(PatientCustomRegistrationSerializer, self).save(request)
        user.is_patient = True
        user.save()
        patient = Patient(
                        patient=user, 
                        age=self.cleaned_data.get('age'), 
                        )
        patient.save()
        return user


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('__all__')
        depth = 1


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('__all__')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        depth = 1