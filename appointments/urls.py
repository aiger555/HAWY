from django.urls import path

from appointments import views

 
urlpatterns = [
    path('', views.AppointmentList.as_view(), name='appointment-list'),
    path('<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
    path('appointments-user/<int:pk>/', views.AppointmentsForUserView.as_view(), name='appointment-user'),
]