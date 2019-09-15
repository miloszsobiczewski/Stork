from django.conf.urls import url
from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path('<int:selected_project>/', views.contacts, name='contacts'),
    path('<int:selected_project>/<int:selected_contact>/', views.contact_details, name='details'),
]
