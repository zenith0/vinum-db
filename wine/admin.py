from django.contrib import admin

# Register your models here.
from .models import Wine

class WineAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Wine, WineAdmin)