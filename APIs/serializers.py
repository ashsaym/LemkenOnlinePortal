from rest_framework import serializers

from Licences.models import LicenceDetails
from CommunicationUnits.models import CommunicationUnit, CommunicationUnitCCIDetails


class serializeCommunicationUnit(serializers.ModelSerializer):
    # Serial_Number = serializers.StringRelatedField(many=True)
    class Meta:
        model = CommunicationUnit
        fields = '__all__'


class serializeCommunicationUnitDetails(serializers.ModelSerializer):
    # Serial_Number = serializers.StringRelatedField(many=True)
    class Meta:
        model = CommunicationUnitCCIDetails
        fields = '__all__'


class serializeLicence(serializers.ModelSerializer):
    # Serial_Number = serializeCommunicationUnit(many=True, read_only=True)
    class Meta:
        model = LicenceDetails
        fields = '__all__'


class serializeOneLicence(serializers.ModelSerializer):
    # Serial_Number = serializeCommunicationUnit(many=True, read_only=True)
    class Meta:
        model = LicenceDetails
        fields = ('Serial_Number', 'license_type', 'LicenceCode', 'expired_on')