from django.db import models
from contact.models import Contact
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
