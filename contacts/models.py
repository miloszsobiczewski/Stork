from django.db import models
from projects.models import Project


class ContactQuerySet(models.QuerySet):
    def for_user(self, user, respect_superuser=False):
        # todo: add superuser exception
        return self.filter(project__owner=user)


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

    objects = ContactQuerySet.as_manager()


class NoteQuerySet(models.QuerySet):
    def for_user(self, user, respect_superuser=False):
        # todo: add superuser exception
        return self.filter(contact__project__owner=user)


class Note(models.Model):
    name = models.CharField(max_length=10)
    text = models.TextField()
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)

    objects = NoteQuerySet.as_manager()
