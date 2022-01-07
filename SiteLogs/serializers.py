from django.contrib.auth import models
from django.db.models.base import Model
from rest_framework import fields, serializers
from APIs.models import LicenceDetails,CommunicationUnit,CommunicationUnitCCIDetails

class serializeCommnucationUnit(serializers.ModelSerializer):
   # Serial_Number = serializers.StringRelatedField(many=True)
    class Meta:
        model = CommunicationUnit
        fields = '__all__'
    
class serializeCommnucationUnitDetails(serializers.ModelSerializer):
       # Serial_Number = serializers.StringRelatedField(many=True)
    class Meta:
        model = CommunicationUnitCCIDetails
        fields = '__all__'
        

class serializeLicence(serializers.ModelSerializer):
    #Serial_Number = serializeCommnucationUnit(many=True, read_only=True)
    class Meta:
        model = LicenceDetails
        fields = '__all__'
        
class serializeOneLicence(serializers.ModelSerializer):
    #Serial_Number = serializeCommnucationUnit(many=True, read_only=True)
    class Meta:
        model = LicenceDetails
        fields = ('Serial_Number', 'license_type', 'LicenceCode','expired_on')