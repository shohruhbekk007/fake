from django.db import models


class Cotegory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Carousel(models.Model):
    title = models.CharField(max_length=68)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    category = models.ForeignKey(Cotegory, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    
    def __str__(self) -> str:
        return self.full_name


class My_plate(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name


class They_about(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title