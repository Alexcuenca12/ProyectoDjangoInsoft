from django.contrib import admin

from .models import en_persona, EnDireccion, EnElectronicos, EnTelefonos

# Register your models here.

admin.site.register(en_persona)
#admin.site.register(en_catalogo)

admin.site.register(EnDireccion)
"""
admin.site.register(EnElectronicos)
admin.site.register(EnTelefonos)

"""


