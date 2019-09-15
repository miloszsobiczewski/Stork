from django.shortcuts import render
from contacts.models import Contact, Note


def contacts(request, selected_project=None):
    # contacts = Contact.objects.filter(project=selected_project)
    contacts = Contact.objects.all()

    context = {
        "project": selected_project,
        "contacts": contacts
    }
    return render(request, "contacts/contacts.html", context)


def contact_details(request, selected_contact=None):
    # contact = Contact.objects.filter(project=selected_contact)
    contact = Contact.objects.first()

    context = {
        "contact": selected_contact,
        "details": contact
    }
    return render(request, "contacts/contacts.html", context)
