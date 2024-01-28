from rest_framework.serializers import ModelSerializer
from .models import Carousel, Cotegory, Contact, My_plate, They_about

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Cotegory
        fields = '__all__'

class Corusels(ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Carousel
        fields='__all__'
    
class ContactSerilazer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class My_platesSerialz(ModelSerializer):
    class Meta:
        model = My_plate
        fields = '__all__'
        
        
class They_aboutSerials(ModelSerializer):
    class Meta:
        model = They_about
        fields = '__all__'