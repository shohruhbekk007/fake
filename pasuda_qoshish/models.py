from django.db import models
from sahifa.models import Toifalash1


class Toifalash(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nomi


class maxsulot_qoshish(models.Model):
    nomi = models.CharField(max_length=100)
    olchami = models.CharField(max_length=20)
    Rasm = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    narxi = models.IntegerField()
    toifasi = models.ForeignKey(Toifalash, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Toifalash1, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nomi
    



# class Set_Pasuda(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi

# class Golf(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi

# class KumushEskiPasuda(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi

# class OqTillaPasuda(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi

# class LacostaPasuda(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi

# class YashilPasuda(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi


# class CofeBreak(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi


# class Inventarlar(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi

# class CofeBreak(models.Model):
#     Sutol = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.Sutol
    
# class MaterialMahsulotlar(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi


# class AlohidaPasuda(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi


# class Stol_stul(models.Model):
#     nomi = models.CharField(max_length=100)
#     stol_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi


# class Materialli_mahsulotlar(models.Model):
#     nomi = models.CharField(max_length=100)
#     tarela_olchami = models.CharField(max_length=20)
#     narxi = models.IntegerField()

#     def __str__(self):
#         return self.nomi