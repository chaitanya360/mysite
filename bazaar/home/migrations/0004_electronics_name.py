# Generated by Django 3.0.5 on 2020-04-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_electronics_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronics',
            name='name',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
