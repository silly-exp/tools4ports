from django.db import models


class Port(models.Model):
    name = models.CharField(max_length=200)
    locode = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Ship(models.Model):
    name = models.CharField(max_length=200)
    imo = models.IntegerField()
    def __str__(self):
        return self.name

class Call(models.Model):
    num = models.CharField(max_length=15)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    eta = models.DateTimeField()
    etd = models.DateTimeField()
    def __str__(self):
        return self.num
