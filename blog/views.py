from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as d
from .models import Carousel, Contact, My_plate, They_about
from .serializer import Corusels, ContactSerilazer, My_platesSerialz, They_aboutSerials
from rest_framework.generics import ListAPIView, CreateAPIView



vaqt = d.now()

def home(request):
    return HttpResponse(f"<h1>{vaqt}</h1>")


class Carusell(ListAPIView):
    queryset = Carousel.objects.all()
    serializer_class = Corusels
 
    
class Contacts(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerilazer


class My_photos(ListAPIView):
    queryset = My_plate.objects.all()
    serializer_class = My_platesSerialz


class They_aboutList(ListAPIView):
    queryset = They_about.objects.all()
    serializer_class = They_aboutSerials