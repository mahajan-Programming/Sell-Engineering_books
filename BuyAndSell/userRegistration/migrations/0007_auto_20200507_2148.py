# Generated by Django 3.0.5 on 2020-05-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0006_auto_20200506_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbook',
            name='BookImage',
            field=models.ImageField(blank=True, upload_to='books'),
        ),
    ]
