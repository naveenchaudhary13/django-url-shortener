from django.contrib import admin
from shortener.models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'preview_long_url', 'click_count', 'expires_at', 'created_at')

    def preview_long_url(self, obj):
        return obj.long_url[:20] + '...' if len(obj.long_url) > 20 else obj.long_url