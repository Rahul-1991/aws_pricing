from django.contrib.auth.models import User
from django.db import models


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)
    aws_access_key = models.CharField(max_length=255, blank=True, null=True)
    aws_auth_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
