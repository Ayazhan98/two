# Generated by Django 2.2.1 on 2019-06-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scopus1', '0003_p_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
    ]