from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

from .serializers import RatingSerializer


class RatingView(APIView):
    
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)