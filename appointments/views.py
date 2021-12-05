from django.http.response import Http404
from django.views import View
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView

from appointments import serializers
from appointments import models



class AppointmentList(APIView):
    """
    Read all appointments, or create new appointment
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_doctor: 
            appointments = models.Appointment.objects.all()
            serializer = serializers.AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Unauthorized to view this page.'})

    def post(self, request):
        serializer = serializers.AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(request.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetail(APIView):
    """
    Read, Update, Delete functionality for one Appointment
    Customers and Employees should only be able to see their own appointments
    """
    permission_classes = [permissions.IsAuthenticated]

    def _get_appointment(self, pk):
        try:
            return models.Appointment.objects.get(pk=pk)
        except models.Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        appointment = self._get_appointment(pk)
        serializer = serializers.AppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk):
        appointment = self._get_appointment(pk)
        serializer = serializers.AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appointment = self._get_appointment(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentsForUserView(APIView):
    """
    Read all appointments for a specific employee_id
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        appointments = models.Appointment.objects.filter(Q(docs_id=pk) | Q(pats_id=pk))
        serializer = serializers.AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)




