# Generated by Django 4.2.7 on 2023-11-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
