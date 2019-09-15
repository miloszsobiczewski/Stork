from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=10)
    text = models.TextField()


class Status(models.Model):
    STATUSES = [
        ("To Do", "todo"),
        ("Doing", "doing"),
        ("Done", "done"),
    ]
    name = models.CharField(max_length=10, choices=STATUSES)


class Contact(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=30)
    note = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
