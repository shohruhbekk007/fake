from django.urls import path
from .views import home, Carusell, Contacts, My_photos, They_aboutList

urlpatterns = [
    path('', home, name="home" ),
    path('corusel', Carusell.as_view(), name="corusellls"),
    path('contact', Contacts.as_view(), name='contacts'),
    path('my_photos', My_photos.as_view(), name='my_photos'),
    path('they_about', They_aboutList.as_view(), name='they_about')
]
