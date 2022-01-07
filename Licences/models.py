import uuid
from datetime import datetime, timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _

# Create your models here.
from CommunicationUnits.models import CommunicationUnit
from coreSettings import settings


class LicenceType(models.Model):
    LicenceType = models.CharField(_('Licence Type Name'), max_length=15, unique=True, primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Licence Type"
        verbose_name_plural = "Licence Types"

    def __str__(self):
        return "{}".format(self.LicenceType)


class LicenceDetails(models.Model):
    LicenceCode = models.UUIDField(_('Licence Code'), max_length=100, unique=True, editable=False,
                                   default=uuid.uuid4, auto_created=True)
    created_on = models.DateTimeField(_('Date of Creation'), auto_now_add=True, editable=False)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Modified_By')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Added_by')
    Serial_Number = models.ForeignKey(CommunicationUnit, on_delete=models.CASCADE)
    expired_on = models.DateTimeField(default=datetime.now() + timedelta(days=3650))
    updated_on = models.DateTimeField(auto_now=True)
    license_type = models.ForeignKey(LicenceType, on_delete=models.CASCADE)
    expired = models.BooleanField(default=False)

    class Meta:
        unique_together = ("Serial_Number", "license_type", "expired")
        verbose_name_plural = "License Details"

    def __str__(self):
        return "{} (License type :  {}  |  code : {})".format(self.Serial_Number, self.license_type, self.LicenceCode)

    @property
    def expired_code(self):
        if now() > self.expired_on:
            self.expired = True
        else:
            self.expired = False
        return self.expired
