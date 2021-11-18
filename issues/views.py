from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import IssueSerializer
from .models import Issue


class IssueAPIView(APIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        issue = Issue.objects.all()
        return issue

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params['id']
            if id != None:
                issue = Issue.objects.get(id=id)
                serializer = IssueSerializer(issue)
        except:
            issues = self.get_queryset()
            serializer = IssueSerializer(issues, many=True)

        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        issue_data = request.data
        new_issue = Issue.objects.create(title=issue_data['title'], body=issue_data['body'])
        new_issue.save()
        
        serializer = IssueSerializer(new_issue)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        issue_object = Issue.objects.get()
    
        data = request.data

        issue_object.title = data['title']
        issue_object.body = data['body']
        issue_object.save()

        serializer = IssueSerializer(issue_object)
        
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        issue_object = Issue.objects.get()
        
        data = request.data

        issue_object.title = data.get('title', issue_object.title)
        issue_object.body = data.get('body', issue_object.body)
        issue_object.save()

        serializer = IssueSerializer(issue_object)

        return Response(serializer.data)