from django.contrib import admin

# Register your models here.
from .models import Client


class ClientAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['street']}),
        (None, {'fields': ['suburb']}),
        (None, {'fields': ['postcode']}),
        (None, {'fields': ['state']}),
        (None, {'fields': ['contact']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['phone']}),
    ]

    list_display = ('name', 'street', 'suburb', 'postcode',
                    'state', 'contact', 'email', 'phone')


admin.site.register(Client, ClientAdmin)
