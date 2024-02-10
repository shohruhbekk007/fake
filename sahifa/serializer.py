from rest_framework.serializers import ModelSerializer
from buyurtmalar.models import  Contact, Product
from pasuda_qoshish.models import Toifalash, maxsulot_qoshish
from .models import Toifalash1, Corusel, Tadbir_lavhalari, Biz_haqimizda, Statiska 


class Toifalash1Serializer(ModelSerializer):
    class Meta:
        model = Toifalash1
        fields = '__all__'

class CoruselSerilazer(ModelSerializer):
    category = Toifalash1Serializer()  # Nomni to'g'riroq yozing
    class Meta:
        model = Corusel
        fields = '__all__'


class Biz_haqimizdaSerilazer(ModelSerializer):
    class Meta:
        model = Biz_haqimizda
        fields = '__all__'


class StatiskaSerilazer(ModelSerializer):
    class Meta:
        model = Statiska
        fields = '__all__'

class Tadbir_lavhaSerilazer(ModelSerializer):
    class Meta:
        model = Tadbir_lavhalari
        fields = '__all__'
        


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


    
class ContactSerilazer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        
class ToifalshSerializer(ModelSerializer):
    class Meta:
        model = Toifalash
        fields = '__all__'


class Maxsulot_qoshishSerialzer(ModelSerializer):
    cotigory = ToifalshSerializer()
    class Meta:
        model = maxsulot_qoshish
        fields = '__all__'

