# Generated by Django 3.0.5 on 2020-05-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(default='', max_length=200)),
                ('Price', models.IntegerField(default=0)),
                ('Year', models.CharField(default='', max_length=10)),
                ('Tag1', models.CharField(choices=[('First Year', 'First year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year')], default='', max_length=20)),
                ('Tag2', models.CharField(choices=[('First Year', 'First Year'), ('CSE', 'CSE'), ('IT', 'IT'), ('Entc', 'Entc'), ('Mech', 'Mech'), ('Instrumentation', 'Instrumentation'), ('Production', 'Production'), ('Chemical', 'Chemical'), ('Electrical', 'Electrical'), ('Mechatronix', 'Mechatronix')], default='', max_length=50)),
                ('BookImage', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
