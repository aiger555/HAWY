from django.db import models
from django.contrib.auth.models import ( 
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone


class UserManager(BaseUserManager):
    
    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **kwargs):
        now = timezone.now()
        if not username:
            raise ValueError('The username is not valid')
        email = self.normalize_email(email)
        user = self.model(
                        username=username, 
                        email=email, 
                        is_active=is_active, 
                        is_staff=is_staff, 
                        is_superuser=is_superuser, 
                        date_joined=now, 
                        **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password, **kwargs):
        return self._create_user(
                                username, email, password, is_active=True, is_staff=False, 
                                is_superuser=False, **kwargs
                                )
        
    
    def create_superuser(self, username, email, password, **kwargs):
        user = self._create_user(
                                username, email, password, is_active=True, is_staff=True, 
                                is_superuser=True, **kwargs)
        user.save(using=self._db)
        return user
        

class Rating(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    receive_newsletter = models.BooleanField(default=False)
    about_me = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True)
    phone = models.CharField(max_length=30)
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE, related_name='rating', null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]



    

 