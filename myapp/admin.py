from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


#admin.site.register(ListeElecteur)
admin.site.register(MonElecteur)

@admin.register(ListeElecteur)
class ListeAdmin(ImportExportModelAdmin):
    pass