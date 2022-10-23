from django.db import models

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):return self.nom

class Ichki(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='ichki_bolimlar')
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, related_name='ichkilari')
    def __str__(self):return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    narx=models.PositiveSmallIntegerField(default=0)
    description=models.CharField(max_length=300)
    guarantee=models.CharField(max_length=50)
    delivery=models.CharField(max_length=50)
    availabilty=models.BooleanField(default=True)
    chegirma=models.PositiveSmallIntegerField(default=0)
    ichki=models.ForeignKey(Ichki, on_delete=models.SET_NULL, null=True)
    def __str__(self):return self.nom

class Rasm(models.Model):
    rasm = models.FileField(upload_to='rasm-mahsulot')
    mahsulot=models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name='rasmlari')