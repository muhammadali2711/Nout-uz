# Generated by Django 4.0.6 on 2022-08-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tg_Nout_uz', '0018_alter_tguser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='last_name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tguser',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]