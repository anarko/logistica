# Generated by Django 3.1.4 on 2020-12-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recupero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='proveedor',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
