# Generated by Django 3.0.5 on 2020-04-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200430_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='number',
            field=models.IntegerField(),
        ),
    ]
