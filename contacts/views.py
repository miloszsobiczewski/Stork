from django.shortcuts import render
from contacts.models import Contact, Note


def contact_details(request, selected_contact=None):
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


def edit_contract_details(request, selected_contact=None):
    if request.method == 'POST':
        pass
    context = {}
    return render(request, "contacts/edit_contacts.html", context)


def edit_note_details(request, selected_note=None):
    if request.method == 'POST':
        pass
    context = {}
    return render(request, "contacts/edit_note.html", context)
