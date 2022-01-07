from django.forms import ModelForm

from Licences.models import LicenceDetails


class CustomAddLicenceForm(ModelForm):
    class Meta:
        model = LicenceDetails
        fields = ('license_type',)


class CustomUpdateLicenceForm(ModelForm):
    class Meta:
        model = LicenceDetails
        fields = ('license_type', 'modified_by', 'added_by',)
