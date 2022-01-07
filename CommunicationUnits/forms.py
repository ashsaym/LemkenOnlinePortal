from django.forms import ModelForm

from CommunicationUnits.models import CommunicationUnit, CommunicationUnitCCIDetails


class CustomADDCommunicationUnitForm(ModelForm):
    class Meta:
        model = CommunicationUnit
        fields = ('SerialNumber', 'added_by',)


class CustomUpdateCommunicationUnitForm(ModelForm):
    class Meta:
        model = CommunicationUnit
        fields = ('SerialNumber', 'added_by',)


class CustomADDCCICommunicationUnitForm(ModelForm):
    class Meta:
        model = CommunicationUnitCCIDetails
        fields = (
            'SerialNumber', 'scrapped', 'device_name', 'machineSerialNo', 'machineNameSeries', 'machineProductionYear',)


class CustomUpdateCCICommunicationUnitForm(ModelForm):
    class Meta:
        model = CommunicationUnitCCIDetails
        fields = (
            'SerialNumber', 'scrapped', 'device_name', 'machineSerialNo', 'machineNameSeries', 'machineProductionYear',)
