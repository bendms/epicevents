from rest_framework.permissions import BasePermission, SAFE_METHODS


from authentication.models import MyUser
from .models import Customer, Contract, Event

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        print("You are here : IsAuthenticated.has_permission")
        print("request.user", request.user)
        print("request.user.is_authenticated", request.user.is_authenticated)
        print("View", view)
        return bool(request.user and request.user.is_authenticated)
    
class IsSalesUser(BasePermission):
    print("You are here : IsSalesUser")

    def has_permission(self, request, view):
        print("You are here : IsSalesUser.has_permission")
        print('MyUser.objects.filter(role="SALES")', MyUser.objects.filter(role="SALES"))
        if request.user in MyUser.objects.filter(role='SALES'):
            return True
    
class IsManager(BasePermission):
    print("You are here : IsManager")
    
    def has_permission(self, request, view):
        if request.user in MyUser.objects.filter(role='MANAGEMENT'):
            return True
        
class IsAssignedToCustomer(BasePermission):
    print("You are here : IsAssignedToCustomer")
    
    def has_permission(self, request, view):
        if view.basename == "customers":
            customer = Customer.objects.get(pk=view.kwargs['pk'])
            print("view.kwargs['pk']", view.kwargs['pk']) 
            if customer.sales_contact == request.user:
                return True               
        elif view.basename == "contract":            
            if view.action == 'list':
                return True
            elif view.action == 'retrieve':
                print("YOU ARE IN THE VIEW.ACTION == RETRIEVE CONDITION")
                print(view.action)
                contract = Contract.objects.get(id=view.kwargs['pk'])
                if request.user == contract.sales_contact:
                    return True
                return False
            elif request.method == "POST" or "PUT":
                print("======REQUEST.DATA=====", request.data)                
                if not request.data:
                    return True
                else:
                    customer = Customer.objects.get(id=request.data['customer'])
                    if request.user == customer.sales_contact:
                        return True
        elif view.basename == "event":
            if view.action == 'list':
                return True
            elif view.action == 'retrieve':
                print("YOU ARE IN THE VIEW.ACTION == RETRIEVE CONDITION")
                print(view.action)
                event = Event.objects.get(id=view.kwargs['pk'])
                if request.user == event.customer.sales_contact:
                    return True
                return False
            elif request.method == "POST" or "PUT":
                if not request.data:
                    return True
                else:
                    customer = Customer.objects.get(id=request.data['customer'])
                    if request.user == customer.sales_contact:
                        return True

class IsAssignedToEvent(BasePermission):
    print("You are here : IsAssignedToEvent")
    
    def has_permission(self, request, view):
        if view.basename == "customers":
            customer = Customer.objects.get(pk=view.kwargs['pk'])
            print("CUSTOMER", customer)
            try:
                events_of_this_customer = Event.objects.filter(customer=customer.id)
                print("EVENT_OF_THIS_CUSTOMER", events_of_this_customer)
                for event in events_of_this_customer:
                    print("EVENT", event)
                    print("EVENT.SUPPORT_CONTACT", event.support_contact)
                    if event.support_contact == request.user:
                        return True
            except:
                return False
        elif view.basename == "event":
            event = Event.objects.get(pk=view.kwargs['pk'])
        print("event", event)
        if request.user == event.support_contact:
            return True
    