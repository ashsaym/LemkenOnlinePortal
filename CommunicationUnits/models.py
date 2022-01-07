from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from coreSettings import settings


class CommunicationUnit(models.Model):
    SerialNumber = models.CharField(_('Serial Number'), max_length=100, unique=True, primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Communication Unit"
        verbose_name_plural = "Communication Units"

    def __str__(self):
        return "{}".format(self.SerialNumber)


class CommunicationUnitCCIDetails(models.Model):
    SerialNumber = models.OneToOneField(CommunicationUnit, on_delete=models.CASCADE, primary_key=True, unique=True)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    device_name = models.CharField(_('Device Name'), max_length=100, null=True, blank=True)
    machineSerialNo = models.CharField(_('Machine Serial Number'), null=True, blank=True, max_length=100)
    machineNameSeries = models.CharField(_('Machine Name Series'), max_length=100, null=True, blank=True)
    machineProductionYear = models.CharField(_('Machine Production Year'), max_length=100, null=True, blank=True)
    scrapped = models.BooleanField()

    class Meta:
        verbose_name = "myCCI Info"
        verbose_name_plural = "myCCI Info"

    def __str__(self):
        return "{}".format(self.SerialNumber)
