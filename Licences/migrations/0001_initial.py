# Generated by Django 4.0.1 on 2022-01-06 15:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CommunicationUnits', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenceType',
            fields=[
                ('LicenceType', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Licence Type Name')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Licence Type',
                'verbose_name_plural': 'Licence Types',
            },
        ),
        migrations.CreateModel(
            name='LicenceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LicenceCode', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='Licence Code')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
                ('expired_on', models.DateTimeField(default=datetime.datetime(2032, 1, 4, 16, 8, 3, 501524))),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('expired', models.BooleanField(default=False)),
                ('Serial_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommunicationUnits.communicationunit')),
                ('added_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to=settings.AUTH_USER_MODEL)),
                ('license_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Licences.licencetype')),
                ('modified_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'License Details',
                'unique_together': {('Serial_Number', 'license_type', 'expired')},
            },
        ),
    ]
