# Generated by Django 3.2 on 2021-06-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='sex',
            field=models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], max_length=10),
        ),
    ]
