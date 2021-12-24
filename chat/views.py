from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView

from .serializers import MessageSerializer

from .models import Message


class MessageList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated: 
            messages = Message.objects.all()
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Unauthorized to view this page.'})

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)