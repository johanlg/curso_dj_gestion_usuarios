# Generated by Django 3.1.7 on 2021-02-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210222_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='genero',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], max_length=1),
        ),
    ]
