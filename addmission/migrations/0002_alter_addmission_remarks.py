# Generated by Django 3.2.6 on 2021-09-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addmission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmission',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]