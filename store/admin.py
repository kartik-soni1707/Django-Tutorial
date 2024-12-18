from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Collection)
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', ]
    list_editable=['unit_price', ]

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable=['membership', ]
