# Generated by Django 4.1 on 2022-09-03 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='coord_servico_x',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='coord_servico_y',
        ),
    ]
