from django.http import HttpResponse
from .serializer import Biz_haqimizdaSerilazer, ProductSerializer, ContactSerilazer, CoruselSerilazer, Maxsulot_qoshishSerialzer, Tadbir_lavhaSerilazer, Toifalash1Serializer, StatiskaSerilazer, ToifalshSerializer
from datetime import datetime as d
from buyurtmalar.models import Contact, Product
from .models import Biz_haqimizda, Corusel, Statiska, Tadbir_lavhalari
from pasuda_qoshish.models import maxsulot_qoshish
from rest_framework.generics import ListAPIView, CreateAPIView



vaqt = d.now()

def home(request):
    return HttpResponse(f"<h1>{vaqt}</h1>")


class Carusell(ListAPIView):
    queryset = Corusel.objects.all()
    serializer_class = CoruselSerilazer
 
    
class Contacts(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerilazer
    
class ProducViews(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


class My_photos(ListAPIView):
    queryset = Tadbir_lavhalari.objects.all()
    serializer_class = Tadbir_lavhaSerilazer


class They_aboutList(ListAPIView):
    queryset = Biz_haqimizda.objects.all()
    serializer_class = Biz_haqimizdaSerilazer
    
    
    
class StatiskaViews(ListAPIView):
    queryset = Statiska.objects.all()
    def get_serializer_class(self):
        return StatiskaSerilazer

    
class MaxsulotViews(ListAPIView):
    queryset = maxsulot_qoshish.objects.all()
    serializer_class = Maxsulot_qoshishSerialzer
