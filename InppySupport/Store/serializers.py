from rest_framework import serializers


class StoreDetailSerializer(serializers.Serializer):

    uid = serializers.CharField(max_length=200)
    store_id = serializers.CharField(max_length=200)
    store_name = serializers.CharField(max_length=200)
    store_type = serializers.CharField(max_length=200)
    store_house_no = serializers.CharField()
    store_land_mark = serializers.CharField(max_length=500)
    store_street = serializers.CharField(max_length=500)
    store_city = serializers.CharField(max_length=200)
    store_pin_code = serializers.CharField()
    store_GST_no = serializers.CharField(max_length=200)
    store_EST_no = serializers.CharField(max_length=200)
    selling_mode = serializers.CharField(max_length=200)
    rules = serializers.CharField(max_length=200)
    store_template = serializers.CharField(max_length=200)
    store_business_email = serializers.CharField(max_length=200)
    store_contact_no = serializers.CharField()


class StoreSettingSerializer(serializers.Serializer):

    store_Online_status = serializers.CharField(max_length=200)
    store_Offline_status = serializers.CharField(max_length=200)
    opening_time = serializers.DateTimeField()
    closing_time = serializers.DateTimeField()
    deliverable_distance = serializers.IntegerField()
    delivery_time = serializers.DateTimeField()
    delivery_cost = serializers.IntegerField()
    store_upi_id = serializers.CharField(max_length=100)
