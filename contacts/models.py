from django.db import models
from projects.models import Project


class Contact(models.Model):
    STATUSES = [
        ("To Do", "todo"),
        ("Doing", "doing"),
        ("Done", "done"),
    ]
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUSES)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)


class Note(models.Model):
    name = models.CharField(max_length=10)
    text = models.TextField()
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
