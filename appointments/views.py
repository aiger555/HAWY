from django.http.response import Http404
from django.views import View
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView

from .serializers import AppointmentSerializer
from .models import Appointment



class AppointmentList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_doctor: 
            appointments = Appointment.objects.all()
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Unauthorized to view this page.'})

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def _get_appointment(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        appointment = self._get_appointment(pk)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk):
        appointment = self._get_appointment(pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appointment = self._get_appointment(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentsForUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        appointments = Appointment.objects.filter(Q(docs_id=pk) | Q(pats_id=pk))
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)




