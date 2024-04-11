from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class AppUser(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=14, unique=True)
    email = models.EmailField(blank=True)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()



class Profile(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)

