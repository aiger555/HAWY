from django.urls import path

from .views import IssueAPIView

    
urlpatterns = [
    path('issues/', IssueAPIView.as_view(), name='issue'),
]
