from django.db import models
from django.contrib.auth.models import User


class ProjectQuerySet(models.QuerySet):
    def for_user(self, user, respect_superuser=False):
        # todo: add superuser exception
        return self.filter(owner=user)


class Project(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    objects = ProjectQuerySet.as_manager()
