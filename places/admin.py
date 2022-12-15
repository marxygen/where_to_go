from django.contrib import admin
from places.models import Place, PlaceImage
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage

    readonly_fields = ["image_preview"]
    fields = ('title', 'image_preview', 'order')

    def image_preview(self, obj):
        return format_html('<img src="{url}" style="max-height: 200px; aspect-ratio={aspect_ratio}"/>'.format(
            url=obj.image.url,
            aspect_ratio=int(obj.image.width / obj.image.height)
        )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
