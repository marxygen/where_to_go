from django.db import models


class PlaceImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок',
                             help_text='Если данное изображение привязано к объекту "Место", будет показано имя объекта. '
                                       'В противном случае, будет показан данный текст')
    image = models.ImageField(verbose_name='Файл изображения')
    order = models.IntegerField(default=1, null=True, blank=True, verbose_name='Порядковый номер', help_text='Если не указан, будет сортирован автоматически')

    class Meta:
        verbose_name = 'Сопроводительное изображение'
        verbose_name_plural = 'Сопроводительные изображения'

    def __str__(self):
        return f'{self.place.first() or self.title}, #{self.order}'


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    images = models.ManyToManyField(PlaceImage, verbose_name='Картинки', blank=True, related_name='place')

    # Might consider using a specialized model (e.g. GeoDjango's Point) instead
    latitude = models.DecimalField(max_digits=22, decimal_places=16, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=22, decimal_places=16, verbose_name='Долгота')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title
