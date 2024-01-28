from django.contrib import admin
from .models import Carousel, Cotegory, Contact, My_plate, They_about

@admin.register(Carousel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


@admin.register(Cotegory)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Contact)

@admin.register(My_plate)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(They_about)
class PostAdmins(admin.ModelAdmin):
    list_display = ('title',)
    