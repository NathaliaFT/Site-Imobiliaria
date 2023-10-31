from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name="index.html"),
    path("", views.contact, name="contact.html"),
    path("", views.properties, name="properties.html"),
    path("", views.property_details, name="property-details.html"),
] 