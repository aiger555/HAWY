from rest_auth.registration.views import RegisterView, APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN)

from .serializers import (
    DoctorCustomRegistrationSerializer, 
    PatientCustomRegistrationSerializer,
    DoctorSerializer,
    PatientSerializer,
    UserSerializer,
    )

from .models import Doctor, Patient, User


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


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, ]  

    def _get_user(self, pk, active_user):
        '''
        This method verifies that the logged in user is the same as
        the one being requested before returning the user object. Or that
        the logged in user is an administrator.
        '''
        error_object = {'error': ''}
        try:
            user = User.objects.get(pk=pk)            
            if user != active_user and active_user.is_staff is False:  
                user = None
                error_object = {'error': 'User is not allowed to view this page.'}
            return user, error_object
        except User.DoesNotExist:
            raise Response(status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        user, err = self._get_user(pk, request.user)
        if err['error'] != '':
            return Response(err, status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
       
        if 'password_submitted' in request.data.keys():
            
            user, err = self._get_user(pk, request.user)
            if err['error'] != '':
                return Response(err, status=status.HTTP_403_FORBIDDEN)
            else:
                serializer = UserSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()

                    user, err = self._get_user(pk, request.user)
                    if err['error'] != '':
                        return Response(err, status=status.HTTP_403_FORBIDDEN)
                    else:
                        user.save()
                    return Response(status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'Password not provided error': 'Must provide a password with a user update.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user, error = self._get_user(pk, request.user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)