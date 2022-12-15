from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    latitude = models.DecimalField(max_digits=22, decimal_places=16, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=22, decimal_places=16, verbose_name='Долгота')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title
