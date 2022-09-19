# Generated by Django 4.0 on 2022-09-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_alter_storedetails_rules_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedetails',
            name='rules',
            field=models.TextField(default='nothing', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='selling_mode',
            field=models.CharField(default='Both', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_EST_no',
            field=models.CharField(default='08AXUPK6638G1XY', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_GST_no',
            field=models.CharField(default='06DXUPK6638G1ZV', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_business_email',
            field=models.CharField(default='laxmi@shoppe.com', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_city',
            field=models.TextField(default='HSR', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_contact_no',
            field=models.IntegerField(default=7689546534, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_house_no',
            field=models.IntegerField(default=34, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_id',
            field=models.CharField(default='si90uj_id0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_land_mark',
            field=models.TextField(default='near agra temple', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_name',
            field=models.CharField(default='laxmi_shoppe', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_pin_code',
            field=models.IntegerField(default=560037, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_street',
            field=models.TextField(default='25c main', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_template',
            field=models.CharField(default='laxmi_template', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_type',
            field=models.CharField(default='variety', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='closing_time',
            field=models.DateTimeField(default='09:00:00 PM', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='deliverable_distance',
            field=models.CharField(default='3km', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='delivery_cost',
            field=models.IntegerField(default=400, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='delivery_time',
            field=models.DateTimeField(default='03:30:00 PM', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='opening_time',
            field=models.DateTimeField(default='09:00:00 AM', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_Offline_status',
            field=models.CharField(default='available', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_Online_status',
            field=models.CharField(default='available', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_city',
            field=models.TextField(default='HSR', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_house_no',
            field=models.IntegerField(default=34, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_id',
            field=models.CharField(default='si90uj_id0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_land_mark',
            field=models.TextField(default='near agra temple', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_latitude',
            field=models.CharField(default='12.972442', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_longitude',
            field=models.CharField(default='77.580643', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_name',
            field=models.CharField(default='laxmi_shoppe', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_pin_code',
            field=models.IntegerField(default=560037, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_street',
            field=models.TextField(default='25c main', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_type',
            field=models.CharField(default='variety', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storesettings',
            name='store_upi_id',
            field=models.CharField(default='nouser-232@paytm', max_length=200, null=True),
        ),
    ]