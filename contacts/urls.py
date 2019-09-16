from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path('<int:selected_contact>/', views.contact_details, name='contact-details'),
    path('<int:selected_contact>/edit/', views.edit_contract_details, name='edit-contract'),
    path('note/<int:selected_note>/edit/', views.edit_note_details, name='edit-note'),
]
