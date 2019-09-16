from django.shortcuts import render
from contacts.models import Contact, Note
from .models import Project


def contacts(request, selected_project=None):
    contacts = Contact.objects.for_user(request.user).filter(project=selected_project)
    project = Project.objects.for_user(request.user).get(pk=selected_project)

    context = {
        "project": project,
        "contacts": contacts
    }
    return render(request, "contacts/contacts.html", context)


def contact_details(request, selected_project=None, selected_contact=None):
    contact = Contact.objects.for_user(request.user).filter(project=selected_contact)
    if not contact:
        return render(request, "contacts/details.html")
    contact = contact.get()
    notes = Note.objects.for_user(request.user).filter(contact=contact.pk)
    context = {
        "contact_id": selected_contact,
        "contact": contact,
        "notes": notes
    }
    return render(request, "contacts/details.html", context)
