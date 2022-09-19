from rest_framework import serializers
from datetime import date

class SupportTicketSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=1000)   
    client_type  = serializers.CharField(max_length=200)
   

class TicketSerializer(serializers.Serializer):
    ticket_id = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=1000)   
    client_type  = serializers.CharField(max_length=200)
    client_id = serializers.CharField(max_length=200)
    store_id = serializers.CharField(max_length=200)
    creation_time = serializers.DateTimeField()
    creation_date = serializers.DateField(default=date.today)           
    status = serializers.CharField(max_length=100)
    lock_status = serializers.BooleanField(default=False)
    resolve_status = serializers.CharField(max_length=100)
    resolve_time = serializers.DateTimeField()
    resolve_date = serializers.DateField(default=date.today)
    current_step = serializers.CharField(max_length=200) 
    active_support_agent = serializers.CharField(max_length=200) 
    