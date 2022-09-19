from django.contrib import admin
from . models import SupportTicket
# Register your models here.
@admin.register(SupportTicket)
class AdminSupportTicket(admin.ModelAdmin):
    list_display = [
        'id',
        'ticket_id',
        'category',
        'subject',
        'description',
        'client_type',
        'client_id',
        'store_id', 
        'creation_time',
        'creation_date',       
        'status', 
        'lock_status', 
        'resolve_status', 
        'resolve_time', 
        'resolve_date', 
        'current_step', 
        'active_support_agent' 
    
        ]



