# Generated by Django 4.1 on 2022-08-17 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tg_Nout_uz', '0015_savat_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savat',
            name='name',
        ),
    ]