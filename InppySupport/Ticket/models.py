from email.policy import default
import imp
from django.db import models
from datetime import date

# Create your models here.

class SupportTicket(models.Model):
    ticket_id = models.TextField(max_length=200)
    category = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)   
    client_type  = models.CharField(max_length=200)
    client_id = models.TextField(max_length=200,null=True,default='dde44iku')
    store_id = models.TextField(max_length=200,null=True,default='yu86ji90k8')
    creation_time = models.DateTimeField(auto_now=True,null=True)
    creation_date = models.DateField(default=date.today,null=True)           
    status = models.CharField(max_length=100,null=True,default=False)
    lock_status = models.BooleanField(default=False,null=True)
    resolve_status = models.CharField(max_length=100,null=True,default='pending')
    resolve_time = models.DateTimeField(auto_now=True,null=True)
    resolve_date = models.DateField(default=date.today,null=True)
    current_step = models.CharField(max_length=200,null=True,default='Processing') 
    active_support_agent = models.CharField(max_length=200,null=True,default='innpy-member') 
    

