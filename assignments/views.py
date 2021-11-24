from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
 
from .models import Assignment, SpecifiedAssignment
from .serializers import AssignmentSerializer, SpecifiedAssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def create(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class SpecifiedAssignmentListView(ListAPIView):
    serializer_class = SpecifiedAssignmentSerializer
    
    def get_queryset(self):
        queryset = SpecifiedAssignment.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(patient__username=username)
        return queryset


class SpecifiedAssignmentCreateView(CreateAPIView):
    serializer_class = SpecifiedAssignmentSerializer
    queryset = SpecifiedAssignment.objects.all()

    def post(self, request):
        serializer = SpecifiedAssignmentSerializer(data=request.data)
        serializer.is_valid()
        specified_assignment = serializer.create(request)
        if specified_assignment:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)