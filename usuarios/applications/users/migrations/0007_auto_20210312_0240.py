# Generated by Django 3.1.7 on 2021-03-12 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210312_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codeRegistro',
            field=models.CharField(max_length=6),
        ),
    ]
