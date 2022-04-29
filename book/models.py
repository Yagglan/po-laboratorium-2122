from django.db import models

# Create your models here.

class typ_dania(models.Model):
    typ = models.CharField(max_length=20)

    def __str__(self):
        return self.typ

class skladniki(models.Model):
    nazwa_skladnika = models.CharField(max_length=20)

    def __str__(self):
        return self.nazwa_skladnika


class danie(models.Model):
    typ_dania = models.ForeignKey(typ_dania, on_delete=models.CASCADE) 
    nazwa_dania = models.CharField(max_length=20)
    przepis = models.ManyToManyField(skladniki)
    def __str__(self):
        return self.nazwa_dania


