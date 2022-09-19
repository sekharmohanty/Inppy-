from django.db import models

# Create your models here.
class StoreDetails(models.Model):
    uid = models.CharField(max_length=200)
    store_id = models.CharField(max_length=200, default="si90uj_id0", null=True)
    store_name = models.CharField(max_length=200, default="laxmi_shoppe", null=True)
    store_type = models.CharField(max_length=200, default="variety", null=True)
    store_house_no = models.IntegerField(default=34, null=True)
    store_land_mark = models.TextField(
        max_length=500, default="near agra temple", null=True
    )
    store_street = models.TextField(max_length=500, default="25c main", null=True)
    store_city = models.TextField(max_length=200, default="HSR", null=True)
    store_pin_code = models.IntegerField(default=560037, null=True)
    store_GST_no = models.CharField(
        max_length=200, default="06DXUPK6638G1ZV", null=True
    )
    store_EST_no = models.CharField(
        max_length=200, default="08AXUPK6638G1XY", null=True
    )
    selling_mode = models.CharField(max_length=200, default="Both", null=True)
    rules = models.TextField(max_length=200, default="nothing", null=True)
    store_template = models.CharField(
        max_length=200, default="laxmi_template", null=True
    )
    store_business_email = models.CharField(
        max_length=200, default="laxmi@shoppe.com", null=True
    )
    store_contact_no = models.IntegerField(default=7689546534, null=True)


class StoreSettings(models.Model):
    store_id = models.CharField(max_length=200, default="si90uj_id0", null=True)
    store_name = models.CharField(max_length=200, default="laxmi_shoppe", null=True)
    store_type = models.CharField(max_length=200, default="variety", null=True)
    store_house_no = models.IntegerField(default=34, null=True)
    store_land_mark = models.TextField(
        max_length=200, default="near agra temple", null=True
    )
    store_street = models.TextField(max_length=200, default="25c main", null=True)
    store_city = models.TextField(max_length=200, default="HSR", null=True)
    store_pin_code = models.IntegerField(default=560037, null=True)
    store_latitude = models.CharField(max_length=200, default="12.972442", null=True)
    store_longitude = models.CharField(max_length=200, default="77.580643", null=True)
    store_Online_status = models.CharField(
        max_length=200, default="available", null=True
    )
    store_Offline_status = models.CharField(
        max_length=200, default="available", null=True
    )
    opening_time = models.DateTimeField(
        max_length=200, default="09:00:00 AM", null=True
    )
    closing_time = models.DateTimeField(
        max_length=200, default="09:00:00 PM", null=True
    )
    deliverable_distance = models.CharField(max_length=200, default="3km", null=True)
    delivery_time = models.DateTimeField(
        max_length=200, default="03:30:00 PM", null=True
    )
    delivery_cost = models.IntegerField(default=400, null=True)
    store_upi_id = models.CharField(
        max_length=200, default="nouser-232@paytm", null=True
    )
