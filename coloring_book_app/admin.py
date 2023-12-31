from django.contrib import admin
from .models import UploadedImage

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at', 'converted_at')
    list_filter = ('uploaded_at', 'converted_at')
    search_fields = ('id',)