# Generated by Django 2.1.7 on 2019-02-18 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_auto_20190218_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]