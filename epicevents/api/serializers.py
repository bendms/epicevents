from .models import Customer, Contract, Event
from authentication.models import MyUser
from django.contrib.auth.models import Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
        
class CustomerSerializer(serializers.ModelSerializer):
    
    contracts = serializers.SerializerMethodField()
    events = serializers.SerializerMethodField()
    
    class Meta:
        model = Customer
        fields = "__all__"
        
    def get_contracts(self, instance):
        queryset = Contract.objects.filter(customer=instance)
        serializer = ContractSerializer(queryset, many=True)
        return serializer.data
        
    def get_events(self, instance):
        queryset = Event.objects.filter(customer=instance)
        serializer = EventSerializer(queryset, many=True)
        return serializer.data
    
class ContractSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Contract
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"