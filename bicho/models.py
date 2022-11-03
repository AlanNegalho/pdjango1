from django.db import models
from loteria.models import Cliente
# Create your models here.

class JogoBicho(models.Model):

    BICHOS = (
        ("1,2,3,4", "Avestruz"),
        ("5,6,7,8", "Àguia"),
        ("9,10,11,12", "Burro"),
        ("13,14,15,16", "Borboleta"),
        ("17,18,19,20", "Cachorro"),
        ("21,22,23,24", "Cabra"),
        ("25,26,27,28", "Carneiro"),
        ("29,30,31,32", "Camelo"),
        ("33,34,35,36", "Cobra"),
        ("37,38,39,40", "Coelho"),
        ("41,42,43,44", "Cavalo"),
        ("45,46,47,48", "Elefante"),
        ("49,50,51,52", "Galo"),
        ("53,54,55,56", "Gato"),
        ("57,58,59,60", "Jacaré"),
        ("61,62,63,64", "Leão"),
        ("65,66,67,68", "Macaco"),
        ("69,70,71,72", "Porco"),
        ("73,74,75,76", "Pavão"),
        ("77,78,79,80", "Perú"),
        ("81,82,83,84", "Touro"),
        ("85,86,87,88", "Tigre"),
        ("89,90,91,92", "Urso"),
        ("93,94,95,96", "Veado"),
        ("97,98,99,00", "Vaca"),
    )


    data = models.DateField()
    bichos = models.JSONField(choices = BICHOS)
    bilhetecliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bichos}'



class Sorteio(models.Model):
    data = models.DateField(auto_now_add=True)
    numeros = models.CharField(max_length=120)
    
    def __str__(self):
        return f'{self.data} - {str(self.numeros)}'