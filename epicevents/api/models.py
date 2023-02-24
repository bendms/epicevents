from django.db import models
from epicevents.settings import AUTH_USER_MODEL as MyUser


class Customer(models.Model):
    
    firstname = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sales_contact = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.company_name + " " + self.firstname + " " + self.lastname

class Contract(models.Model):
    
    sales_contact = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()
    
    def __str__(self):
        return "Contrat " + str(self.customer) + " - " + str(self.amount) + "€ géré par " + str(self.sales_contact)

class Event(models.Model):
    
    EVENT_STATUS_CHOICES = [
        ("PLANNED", "Planifié"),
        ("ACCOMPLISHED", "Réalisé"),
    ]    
        
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    event_status = models.CharField(max_length=50, choices=EVENT_STATUS_CHOICES)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.customer) + str(self.event_date)

# class EventStatus(models.Model):
    
#     EVENT_STATUS_CHOICES = [
#         ("PLANNED", "Planifié"),
#         ("ACCOMPLISHED", "Réalisé"),
#     ]
#     event_status = models.CharField(max_length=50, choices=EVENT_STATUS_CHOICES)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)    