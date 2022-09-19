import string
from django.http import JsonResponse
from .models import SupportTicket
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import SupportTicketSerializer, TicketSerializer
import uuid
import io

# Create your views here.
@csrf_exempt
def create_ticket(request):
    """
    creates ticket for each request.

    :param:request
    :return:json string
    """
    try:
        if request.method == "POST":
            ticket_id = str(uuid.uuid4())[0:8]
            request_id = str(uuid.uuid4())[0:10]
            machine_id = str(uuid.uuid4())[0:12]
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            print(python_data)
            token = python_data.get("token_data")
            uid = python_data["token_data"]["uid"]
            serializer = SupportTicketSerializer(data=python_data)
            if serializer.is_valid(raise_exception=True):
                cat = serializer.data.get("category")
                sub = serializer.data.get("subject")
                des = serializer.data.get("description")
                cli = serializer.data.get("client_type")
                obj = SupportTicket(
                    ticket_id=ticket_id,
                    category=cat,
                    subject=sub,
                    description=des,
                    client_type=cli,
                    client_id=uid,
                )
                obj.save()

                com_data = SupportTicket.objects.get(ticket_id=ticket_id)
                serializer_data = TicketSerializer(com_data)
                tic = serializer_data.data.get("ticket_id")
                c_at = serializer_data.data.get("category")
                s_ub = serializer_data.data.get("subject")
                d_sc = serializer_data.data.get("description")
                c_type = serializer_data.data.get("client_type")
                c_id = serializer_data.data.get("client_id")
                s_id = serializer_data.data.get("store_id")
                c_time = serializer_data.data.get("creation_time")
                c_date = serializer_data.data.get("creation_date")
                s_tus = serializer_data.data.get("status")
                l_tus = serializer_data.data.get("lock_status")
                r_tus = serializer_data.data.get("resolve_status")
                r_time = serializer_data.data.get("resolve_time")
                r_date = serializer_data.data.get("resolve_date")
                c_step = serializer_data.data.get("current_step")
                ac_agent = serializer_data.data.get("active_support_agent")

                return JsonResponse(
                    {
                        "status_code": 200,
                        "msg": {
                            "ticket_id": tic,
                            "category": c_at,
                            "subject": s_ub,
                            "description": d_sc,
                            "client_type": c_type,
                            "client_id": c_id,
                            "store_id": s_id,
                            "creation_time": c_time,
                            "creation_date": c_date,
                            "status": s_tus,
                            "lock_status": l_tus,
                            "resolve_status": r_tus,
                            "resolve_time": r_time,
                            "resolve_date": r_date,
                            "current_step": c_step,
                            "active_support_agent": ac_agent,
                        },
                        "token": token,
                        "request_id": request_id,
                        "machine_id": machine_id,
                    }
                )

    except Exception as e:
        print(e)
