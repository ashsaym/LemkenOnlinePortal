# Generated by Django 4.0.1 on 2022-01-06 15:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Licences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licencedetails',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Added_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='licencedetails',
            name='expired_on',
            field=models.DateTimeField(default=datetime.datetime(2032, 1, 4, 16, 33, 31, 699898)),
        ),
        migrations.AlterField(
            model_name='licencedetails',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Modified_By', to=settings.AUTH_USER_MODEL),
        ),
    ]
