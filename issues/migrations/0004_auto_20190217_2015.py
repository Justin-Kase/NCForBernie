# Generated by Django 2.1.7 on 2019-02-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_issue_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]