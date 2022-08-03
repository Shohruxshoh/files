from django.contrib import admin
from .models import Files
# Register your models here.

class FilesAdmin(admin.ModelAdmin):
    list_display = ['user', 'file_name', 'files', 'created', 'updated']

admin.site.register(Files, FilesAdmin)
