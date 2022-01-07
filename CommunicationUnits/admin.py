from django.contrib import admin

from CommunicationUnits.forms import CustomADDCommunicationUnitForm, CustomUpdateCommunicationUnitForm, \
    CustomADDCCICommunicationUnitForm, CustomUpdateCCICommunicationUnitForm
from CommunicationUnits.models import CommunicationUnit, CommunicationUnitCCIDetails


# Register your models here.
@admin.register(CommunicationUnit)
class CommunicationUnitAdmin(admin.ModelAdmin):
    add_form = CustomADDCommunicationUnitForm
    form = CustomUpdateCommunicationUnitForm
    model = CommunicationUnit
    list_display = ('SerialNumber', 'added_by', 'created_on', 'updated_on',)
    list_filter = ('SerialNumber', 'added_by', 'created_on', 'updated_on',)
    fieldsets = (
        (None, {'fields': ('SerialNumber', 'added_by')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('SerialNumber', 'updated_on', 'added_by')}
         ),
    )
    search_fields = ('SerialNumber',)
    ordering = ('SerialNumber',)


class CommunicationUnitCCIDetailsAdmin(admin.ModelAdmin):
    add_form = CustomADDCCICommunicationUnitForm
    form = CustomUpdateCCICommunicationUnitForm
    model = CommunicationUnitCCIDetails
    list_display = (
        'SerialNumber', 'scrapped', 'device_name', 'machineSerialNo', 'machineNameSeries', 'machineProductionYear',
        'updated_on',)
    list_filter = (
        'SerialNumber', 'scrapped', 'device_name', 'machineSerialNo', 'machineNameSeries', 'machineProductionYear',
        'updated_on',)
    fieldsets = (
        (None, {'fields': (
            'scrapped', 'SerialNumber', 'device_name', 'machineSerialNo', 'machineNameSeries',
            'machineProductionYear',)}),
    )
    search_fields = ('SerialNumber__SerialNumber',)
    ordering = ('SerialNumber',)


admin.site.register(CommunicationUnitCCIDetails, CommunicationUnitCCIDetailsAdmin)