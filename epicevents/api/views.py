from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from .models import Customer, Contract, Event
from authentication.models import MyUser
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, CustomerSerializer, ContractSerializer, EventSerializer


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
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    
    def list(self, request):
        queryset = Customer.objects.filter()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Customer.objects.filter()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    
    def list(self, reqiest):
        queryset = Contract.objects.filter()
        serializer = ContractSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Contract.objects.filter()
        contract = get_object_or_404(queryset, pk=pk)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)
    
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    
    def list(self, request):
        queryset = Event.objects.filter()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Event.objects.filter()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)