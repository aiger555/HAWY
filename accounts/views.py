from rest_framework import viewsets
from rest_framework.response import Response
from .models import Rating, User
from .serializer import RatingSerializer, UserDetailsSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserDetailsSerializer


    def get_queryset(self):
        users = User.objects.all()
        return users


    def create(self, request, *args, **kwargs):
        user_data = request.data

        new_rating = Rating.objects.create(
                                        likes=user_data['rating']['likes'], 
                                        dislikes=user_data['rating']['dislikes']
                                        )
        new_rating.save()

        new_user = User.objects.create(
                                    username=user_data['username'], 
                                    email=user_data['email'],
                                    first_name=user_data['first_name'],
                                    last_name=user_data['last_name'],
                                    is_active=user_data['is_active'],
                                    is_staff=user_data['is_staff'],
                                    is_superuser=user_data['is_superuser'],
                                    date_joined=user_data['date_joined'],
                                    receive_newsletter=user_data['receive_newsletter'],
                                    about_me=user_data['about_me'],
                                    profile_image=user_data['profile_image'],
                                    phone=user_data['phone'], 
                                    rating=new_rating
                                    )
        new_user.save()
        
        serializer = UserDetailsSerializer(new_user)

        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    serialzer_class = RatingSerializer

    def get_queryset(self):
        rating = Rating.objects.all()
        return rating