# Generated by Django 2.2.3 on 2020-08-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_auto_20200816_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(max_length=200, verbose_name='название покемона на русском языке'),
        ),
    ]