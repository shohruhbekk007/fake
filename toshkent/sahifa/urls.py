from django.urls import path
from .views import home, Carusell,  My_photos, They_aboutList, Contacts, ProducViews, MaxsulotViews, StatiskaViews

urlpatterns = [
    path('', home, name="home" ),
    path('corusel', Carusell.as_view(), name="corusellls"),
    path('contact', Contacts.as_view(), name='contacts'),
    path('Otkazilgan_tadbirlar', My_photos.as_view(), name='my_photos'),
    path('Biz_haqimizda', They_aboutList.as_view(), name='they_about'),
    path('products', ProducViews.as_view(), name='product'),
    path('maxsulot_qoshish', MaxsulotViews.as_view(), name='maxsulot'),
    path('statiska', StatiskaViews.as_view(), name='statiska'),   
]
