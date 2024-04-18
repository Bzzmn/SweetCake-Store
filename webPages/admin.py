from django.contrib import admin
from .models import Torta, ContactForm

# Register your models here.

class TortaAdmin(admin.ModelAdmin):
    exclude = ('slug', 'torta_uuid',)
admin.site.register(Torta, TortaAdmin)

admin.site.register(ContactForm)