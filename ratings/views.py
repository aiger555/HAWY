from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView

from django.http.response import Http404

from ratings import serializers

from ratings import models


class RatingList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_patient: 
            ratings = models.Rating.objects.all()
            serializer = serializers.RatingSerializer(ratings, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Unauthorized to view this page.'})

    def post(self, request):
        serializer = serializers.RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def _get_rating(self, pk):
        try:
            return models.Rating.objects.get(pk=pk)
        except models.Rating.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rating = self._get_rating(pk)
        serializer = serializers.RatingSerializer(rating)
        return Response(serializer.data)

    def put(self, request, pk):
        rating = self._get_rating(pk)
        serializer = serializers.RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rating = self._get_rating(pk)
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


