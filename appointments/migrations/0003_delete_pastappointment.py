# Generated by Django 3.2.9 on 2021-12-07 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20211205_1837'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PastAppointment',
        ),
    ]
