# Generated by Django 2.1.7 on 2019-02-14 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOrdemServico', '0003_auto_20190214_1522'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tipoSerico',
            new_name='tipoServico',
        ),
    ]
