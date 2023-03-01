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
        try:
            customer = Customer.objects.get(pk=view.kwargs['pk'])
            print("customer", customer)
            contract = Contract.objects.get(pk=view.kwargs['pk'])
            print("contract", contract)
            if request.user == customer.sales_contact or request.user == contract.customer.sales_contact:
                return True
        except:
            return False

class IsAssignedToEvent(BasePermission):
    print("You are here : IsAssignedToEvent")
    
    def has_permission(self, request, view):
        event = Event.objects.get(pk=view.kwargs['pk'])
        print("event", event)
        if request.user == event.support_contact:
            return True
    
        
