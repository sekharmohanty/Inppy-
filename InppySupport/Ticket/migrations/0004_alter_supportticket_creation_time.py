# Generated by Django 4.0 on 2022-09-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0003_alter_supportticket_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='creation_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]