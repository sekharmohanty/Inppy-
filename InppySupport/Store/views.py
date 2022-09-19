import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Store.serializers import StoreDetailSerializer, StoreSettingSerializer
from .models import StoreDetails, StoreSettings
import io


@csrf_exempt
def store_details(request):
    """
    Retrieve store details for support member

    :param:request
    :return:json string
    """
    try:
        if request.method == "POST":
            request_id = str(uuid.uuid4())[0:10]
            machine_id = str(uuid.uuid4())[0:12]
            print(request_id, machine_id)
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            token = python_data.get("token_data")
            store_id = python_data.get("store_id")
            print(store_id)
            store_obj = StoreDetails.objects.using("new").get(store_id=store_id)
            print(store_obj)
            serializer = StoreDetailSerializer(store_obj)
            print(serializer.data)
            uid = serializer.data.get("uid")
            s_id = serializer.data.get("store_id")
            s_name = serializer.data.get("store_name")
            s_type = serializer.data.get("store_type")
            s_house_no = serializer.data.get("store_house_no")
            s_land_mark = serializer.data.get("store_land_mark")
            s_street = serializer.data.get("store_street")
            s_city = serializer.data.get("store_city")
            s_pin_code = serializer.data.get("store_pin_code")
            s_GST_no = serializer.data.get("store_GST_no")
            s_EST_no = serializer.data.get("store_EST_no")
            s_mode = serializer.data.get("selling_mode")
            rules = serializer.data.get("rules")
            s_template = serializer.data.get("store_template")
            s_business_email = serializer.data.get("store_business_email")
            s_contact_no = serializer.data.get("store_contact_no")

            s_obj = StoreSettings.objects.using("new").get(store_id=store_id)
            s_serializer = StoreSettingSerializer(s_obj)
            s_online = s_serializer.data.get("store_Online_status")
            s_offline = s_serializer.data.get("store_Offline_status")
            s_opening = s_serializer.data.get("opening_time")
            s_closing = s_serializer.data.get("closing_time")
            d_distance = s_serializer.data.get("deliverable_distance")
            d_time = s_serializer.data.get("delivery_time")
            d_cost = s_serializer.data.get("delivery_cost")
            s_upi_id = s_serializer.data.get("store_upi_id")

            return JsonResponse(
                {
                    "status_code": 200,
                    "msg": {
                        "uid": uid,
                        "store_id": s_id,
                        "store_GST_no": s_GST_no,
                        "store_EST_no": s_EST_no,
                        "selling_mode": s_mode,
                        "rules": rules,
                        "store_template": s_template,
                        "store_business_email": s_business_email,
                        "store_contact_no": s_contact_no,
                        "store_name": s_name,
                        "store_type": s_type,
                        "store_house_no": s_house_no,
                        "store_land_mark": s_land_mark,
                        "store_street": s_street,
                        "store_city": s_city,
                        "store_pin_code": s_pin_code,
                        "store_Online_status": s_online,
                        "store_Offline_status": s_offline,
                        "opening_time": s_opening,
                        "closing_time": s_closing,
                        "deliverable_distance": d_distance,
                        "delivery_time": d_time,
                        "delivery_cost": d_cost,
                        "store_upi_id": s_upi_id,
                    },
                    "token": token,
                    "request_id": request_id,
                    "machine_id": machine_id,
                }
            )

    except Exception as e:
        print(e)
