from django.shortcuts import render
from .models import Project
from contacts.models import Contact, Note


def projects(request):
    projects = Project.objects.for_user(request.user)

    context = {
        "projects": projects,
    }
    return render(request, "projects/projects.html", context)


def project_details(request, selected_project=None):
    contacts = Contact.objects.for_user(request.user).filter(project=selected_project)
    project = Project.objects.for_user(request.user).get(pk=selected_project)

    context = {
        "project": project,
        "contacts": contacts
    }
    return render(request, "contacts/contacts.html", context)


def edit_project_details(request, selected_project=None):
    pass
