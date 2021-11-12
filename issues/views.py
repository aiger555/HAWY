from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import IssueSerializer
from .models import Issue


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        issue = Issue.objects.all()
        return issue

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        issues = Issue.objects.filter(title=params['pk'])
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)