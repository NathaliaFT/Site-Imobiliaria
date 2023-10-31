from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("properties/", views.properties, name="properties"),
    path("property-details/", views.property_details, name="property-details"),
]
