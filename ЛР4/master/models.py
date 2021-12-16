from django.db import models


class Creat(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
