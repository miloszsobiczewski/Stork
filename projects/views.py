from django.shortcuts import render
from .models import Project
from contacts.models import Contact, Note


def projects(request):
    projects = Project.objects.all()
    contacts = Contact.objects.all()

    context = {
        "projects": projects,
        "contacts": contacts
    }
    return render(request, "projects/projects.html", context)
