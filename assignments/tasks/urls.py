from rest_framework.routers import DefaultRouter

from assignments.views import AssignmentViewSet


router = DefaultRouter()
router.register('', AssignmentViewSet, basename='users')
urlpatterns = router.urls