from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extending the AbstractUser model does not effect the auth system, so it's just for adding additional fields.
# Had I extended the AbstractBaseUser model, I would have needed to create a new User Manager model, but tcould then
# adjust what fields are needed to login etc.


# Create your models here.
class CustomUser(AbstractUser):

    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("inside create user receiver")
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender='users.CustomUser')
