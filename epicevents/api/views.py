from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from .models import Customer, Contract, Event
from authentication.models import MyUser
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

from .serializers import UserSerializer, GroupSerializer, CustomerSerializer, ContractSerializer, EventSerializer
from .permissions import IsAuthenticated, IsSalesUser, IsManager, IsAssignedToCustomer, IsAssignedToEvent



class UserViewSet(viewsets.ModelViewSet):
    "API endpoint that allows users to be viewed or edited"
    queryset = MyUser.objects.all().order_by('date_created')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    "API endpoint that allows groups to be viewed or edited"
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ['company_name', 'email']
    search_fields = ['company_name', 'email']
    
    # def get_queryset(self):
    #     user = self.request.user
    #     print('SELF.ACTION_IN_GET_QUERYSET_METHOD', self.action)
    #     return Customer.objects.filter(sales_contact=user.id)
    def get_queryset(self):
        return Customer.objects.all()
       
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
            return [permission() for permission in permission_classes]
        elif self.action == 'retrieve':
            permission_classes = [IsAssignedToCustomer]
            return [permission() for permission in permission_classes]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAssignedToCustomer & IsSalesUser]
            return [permission() for permission in permission_classes]
        elif self.action == 'create':
            permission_classes = [IsSalesUser]
            return [permission() for permission in permission_classes]
        elif self.action == 'destroy':
            permission_classes = [IsManager]
            return [permission() for permission in permission_classes]
        return super().get_permissions()
      
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer_class = CustomerSerializer(queryset, many=True)
        headers = self.get_success_headers(serializer_class.data)
        return Response(serializer_class.data, status=status.HTTP_200_OK, headers=headers)
    
    def retrieve(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filterset_fields = ['customer__company_name', 'customer__email', 'date_created', 'amount']
    search_fields = ['customer__company_name', 'customer__email', 'date_created', 'amount']
        
    def get_queryset(self):
        return Contract.objects.all()
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
            return [permission() for permission in permission_classes]
        elif self.action == 'retrieve':
            permission_classes = [IsAssignedToCustomer]
            return [permission() for permission in permission_classes]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAssignedToCustomer & IsSalesUser]
            return [permission() for permission in permission_classes]
        elif self.action == 'create':
            permission_classes = [IsSalesUser]
            return [permission() for permission in permission_classes]
        elif self.action == 'destroy':
            permission_classes = [IsManager]
            return [permission() for permission in permission_classes]
        return super().get_permissions()
        
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ContractSerializer(queryset, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        
    
    def retrieve(self, request, pk=None):
        queryset = Contract.objects.filter()
        contract = get_object_or_404(queryset, pk=pk)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)
    
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filterset_fields = ['customer__company_name', 'customer__email', 'event_date']
    search_fields = ['customer__company_name', 'customer__email', 'event_date']
    
    def get_queryset(self):
        return Event.objects.all()
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
            return [permission() for permission in permission_classes]
        elif self.action == 'retrieve':
            permission_classes = [IsAssignedToCustomer | IsAssignedToEvent]
            return [permission() for permission in permission_classes]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAssignedToCustomer | IsAssignedToEvent]
            return [permission() for permission in permission_classes]
        elif self.action == 'create':
            permission_classes = [IsSalesUser]
            return [permission() for permission in permission_classes]
        elif self.action == 'destroy':
            permission_classes = [IsManager]
            return [permission() for permission in permission_classes]
        return super().get_permissions()
        
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        print("queryset", queryset)
        event = get_object_or_404(queryset, pk=pk)
        print("event", event)
        serializer = EventSerializer(event)
        print("serializer", serializer)
        return Response(serializer.data)