# Generated by Django 2.1.2 on 2018-10-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='rarity',
            field=models.CharField(max_length=255, verbose_name='rarity'),
        ),
    ]
