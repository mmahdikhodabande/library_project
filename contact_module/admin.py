from django.contrib import admin
from . import models


# Register your models here.


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'full_name', 'is_read_by_admin']
    list_editable = ['is_read_by_admin']


admin.site.register(models.ContactUsModel, ContactModelAdmin)
