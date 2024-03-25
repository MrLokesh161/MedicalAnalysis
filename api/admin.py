from django.contrib import admin
from .models import Patient, Fractured, NonFractured

class PatientAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Phone', 'result', 'Xray']
    search_fields = ['Name', 'Email', 'Phone']
    list_filter = ['result']

class FractureAdmin(admin.ModelAdmin):
    list_display = ['description_fractured']

class NonFractureAdmin(admin.ModelAdmin):
    list_display = ['description_not_fractured']

admin.site.register(NonFractured, NonFractureAdmin)
admin.site.register(Fractured, FractureAdmin)
admin.site.register(Patient, PatientAdmin)
