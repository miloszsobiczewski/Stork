from django.shortcuts import render
from contacts.models import Contact, Note
from .models import Project


def contacts(request, selected_project=None):
    contacts = Contact.objects.filter(project=selected_project)
    project = Project.objects.get(pk=selected_project)

    context = {
        "project": project,
        "contacts": contacts
    }
    return render(request, "contacts/contacts.html", context)


def contact_details(request, selected_project=None, selected_contact=None):
    contact = Contact.objects.get(project=selected_contact)
    notes = Note.objects.filter(contact=contact.pk).order_by("-pk")
    context = {
        "contact_id": selected_contact,
        "contact": contact,
        "notes": notes
    }
    return render(request, "contacts/details.html", context)
