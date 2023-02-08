from django.db import models
from tinymce.models import HTMLField


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name="Файл изображения")
    place = models.ForeignKey(
        to="places.Place",
        on_delete=models.CASCADE,
        verbose_name="Место",
        related_name="images",
        null=True,
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        verbose_name="Порядковый номер",
        help_text="Если не указан, будет сортирован автоматически",
        db_index=True,
    )

    class Meta:
        verbose_name = "Сопроводительное изображение"
        verbose_name_plural = "Сопроводительные изображения"
        ordering = ("order",)
        unique_together = ("image", "place", "order")

    def __str__(self):
        return f"{self.place.title}, #{self.order}"


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    short_description = models.TextField(verbose_name="Короткое описание")
    long_description = HTMLField(verbose_name="Длинное описание")

    # Might consider using a specialized model (e.g. GeoDjango's Point) instead
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, verbose_name="Широта"
    )
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, verbose_name="Долгота"
    )

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.title
