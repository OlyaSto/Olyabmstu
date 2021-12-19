from django.db import models


class Rases(models.Model):
    name = models.CharField(max_length=30)
    discription = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rases'


class Cans(models.Model):
    idrases = models.IntegerField()
    cans = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cans'