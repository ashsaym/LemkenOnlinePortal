from django.contrib import admin

# Register your models here.
from Licences.forms import CustomAddLicenceForm, CustomUpdateLicenceForm
from Licences.models import LicenceType, LicenceDetails


@admin.register(LicenceType)
class LicenceTypeAdmin(admin.ModelAdmin):
    list_display = ('LicenceType', 'added_by', 'created_on', 'updated_on',)
    list_filter = ('LicenceType', 'added_by', 'created_on', 'updated_on',)
    fieldsets = (
        (None, {'fields': ('LicenceType', 'added_by')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('LicenceType', 'updated_on', 'added_by')}
         ),
    )
    search_fields = ('LicenceType',)
    ordering = ('LicenceType',)


@admin.register(LicenceDetails)
class LicenceDetailsAdmin(admin.ModelAdmin):
    add_form = CustomAddLicenceForm
    form = CustomUpdateLicenceForm
    model = LicenceDetails
    list_display = (
        'Serial_Number', 'license_type', 'expired', 'expired_on', 'updated_on', 'created_on', 'modified_by', 'added_by',
        'LicenceCode',)
    list_filter = (
        'Serial_Number', 'license_type', 'expired', 'expired_on', 'updated_on', 'created_on', 'modified_by', 'added_by',
        'LicenceCode',)
    fieldsets = (
        (None, {'fields': ('Serial_Number', 'license_type', 'modified_by', 'added_by', 'expired_on', 'expired')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('Serial_Number', 'license_type', 'modified_by', 'added_by',)}
         ),
    )
    search_fields = ('Serial_Number__SerialNumber',)
    ordering = ('Serial_Number',)
