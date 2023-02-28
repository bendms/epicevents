from rest_framework.permissions import BasePermission, SAFE_METHODS


from authentication.models import MyUser
from .models import Customer

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
        print(view.kwargs['pk'])
        customer = Customer.objects.get(pk=view.kwargs['pk'])
        if request.user == customer.sales_contact:
            return True