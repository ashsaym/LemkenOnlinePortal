from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from Licences.models import LicenceDetails
from CommunicationUnits.models import CommunicationUnit, CommunicationUnitCCIDetails

from APIs.serializers import serializeLicence, serializeOneLicence, serializeCommunicationUnitDetails,serializeCommunicationUnit
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PingViewSet(GenericViewSet, ListModelMixin):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response(
            data={"connect": True},
            status=HTTP_200_OK
        )


class ConnectionCheck(GenericViewSet, ListModelMixin):
    def list(self, request, *args, **kwargs):
        return Response(
            data={"connect": True},
            status=HTTP_200_OK
        )


class ShowLicenceDetailsView(GenericViewSet, ListModelMixin):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        licenseObj = LicenceDetails.objects.all()
        serializerLicenceObj = serializeLicence(licenseObj, many=True)
        return Response(serializerLicenceObj.data, status=HTTP_200_OK)


@api_view(['get'])
def ShowOneLicenceDetailsForMachine(request, Serial_Number, license_type):
    licenseObj = LicenceDetails.objects.filter(Serial_Number=Serial_Number, license_type=license_type)
    serializerLicenceObj = serializeOneLicence(licenseObj, many=True)
    ResponseData = Response(serializerLicenceObj.data)
    return ResponseData


class CommunicationUnitListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transformers = CommunicationUnit.objects.all()
        serializer = serializeCommunicationUnit(transformers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializeCommunicationUnit(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunicationUnitDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):

        try:
            return CommunicationUnitCCIDetails.objects.get(pk=pk)
        except CommunicationUnitCCIDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        myCCIDetails = self.get_object(pk)
        serializer = serializeCommunicationUnitDetails(CommunicationUnitCCIDetails)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = serializeCommunicationUnitDetails(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        myCCIDetails = self.get_object(pk)
        serializer = serializeCommunicationUnitDetails(CommunicationUnitCCIDetails, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        myCCIDetails = self.get_object(pk)
        serializer = serializeCommunicationUnitDetails(myCCIDetails,
                                                       data=request.data,
                                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        communicationUnit = self.get_object(pk)
        communicationUnit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
