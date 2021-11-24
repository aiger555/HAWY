from django.urls import path
# from rest_framework.routers import DefaultRouter

from assignments.views import SpecifiedAssignmentListView, SpecifiedAssignmentCreateView


# router = DefaultRouter()
# router.register('', AssignmentViewSet, basename='users')
urlpatterns = [
    path('specified/', SpecifiedAssignmentListView.as_view()),
    path('create/', SpecifiedAssignmentCreateView.as_view()),
]