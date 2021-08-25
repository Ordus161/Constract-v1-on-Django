from django.contrib import admin
from .models import Application, ConstructionSite, Photo


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'quantity', 'area', 'link', 'item', 'shop', 'created_at', 'updated_at', 'is_executed')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'brand', 'shop')
    list_editable = ('is_executed',)
    list_filter = ('created_at', 'is_executed')


class ConstructionSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'numb')
    list_display_links = ('id', 'address')
    search_fields = ('address', 'numb')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill')
    list_display_links = ('id', 'bill')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(ConstructionSite)
admin.site.register(Photo)
