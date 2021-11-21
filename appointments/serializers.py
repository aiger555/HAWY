from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from .models import Psychologist, Patient


class PsychologistCustomRegistrationSerializer(RegisterSerializer):
    psychologist = serializers.PrimaryKeyRelatedField(read_only=True)
    issue = serializers.RelatedField(read_only=True)
    age = serializers.IntegerField(required=True)
    experience_of_work = serializers.CharField(required=True)
    registration_date = serializers.DateTimeField(read_only=True, format="%d-%m-%Y %H:%M")

    def get_cleaned_data(self):
            data = super(PsychologistCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'issue' : self.validated_data.get('issue', ''),
                'age': self.validated_data.get('age', ''),
                'experience_of_work': self.validated_data.get('experience_of_work', ''),
                'registration_date': self.validated_data.get('registration_date', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(PsychologistCustomRegistrationSerializer, self).save(request)
        user.is_psychologist = True
        user.save()
        psychologist = Psychologist(
            psychologist=user,
            issue=self.cleaned_data.get('issue'), 
            age=self.cleaned_data.get('age'),
            experience_of_work=self.cleaned_data.get('experience_of_work'),
            registration_date=self.cleaned_data.get('registration_date'),
            )
        psychologist.save()
        return user


class PatientCustomRegistrationSerializer(RegisterSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    doctor = serializers.RelatedField(read_only=True)
    name = serializers.CharField(required=True)
    registration_date = serializers.DateTimeField(read_only=True, format="%d-%m-%Y %H:%M")
    age = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
            data = super(PatientCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'doctor' : self.validated_data.get('doctor', ''),
                'name': self.validated_data.get('name', ''),
                'registration_date': self.validated_data.get('registration_date', ''),
                'age': self.validated_data.get('age', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(PatientCustomRegistrationSerializer, self).save(request)
        user.is_patient = True
        user.save()
        patient = Patient(
            patient=user,
            doctor=self.cleaned_data.get('doctor'), 
            name=self.cleaned_data.get('name'),
            registration_date=self.cleaned_data.get('registration_date'),
            age=self.cleaned_data.get('age'),
            )
        patient.save()
        return user