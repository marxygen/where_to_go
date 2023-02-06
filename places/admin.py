from django.contrib import admin
from places.models import Place, PlaceImage
from django.utils.html import format_html
from adminsortable2.admin import (
    SortableTabularInline,
    SortableAdminMixin,
    SortableAdminBase,
)


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class PlaceImageInline(SortableTabularInline):
    """Inline Widget to display place images right in `Place` model admin"""

    model = PlaceImage

    readonly_fields = ["image_preview"]
    fields = ("image_preview", "order")

    def image_preview(self, image):
        return format_html(
            '<img src="{url}" style="max-height: 200px; aspect-ratio={aspect_ratio}"/>',
            url=image.image.url,
            aspect_ratio=int(image.image.width / image.image.height),
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline]
