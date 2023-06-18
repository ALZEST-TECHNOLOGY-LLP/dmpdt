from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_pass_token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.EmailField("", max_length=254)
    pass_token = models.CharField("", max_length=500)

    def __str__(self):
        return self.user.username