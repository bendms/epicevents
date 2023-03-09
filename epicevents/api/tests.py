from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from api.models import Customer, Contract, Event
from authentication.models import MyUser

# class CustomerTests(APITestCase):
    
#     token = Token.objects.get(user__email='sales1@epicevents.com')
#     client = APIClient()
#     client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
#     def test_get_existing_customer(self):
#         url = reverse('customers-list')
#         response = self.client.get(url, self.client)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    # def test_create_customer(self):
    #     url = reverse('customers')
    #     data = {'email': 'contact@microsoft.com', 'company_name': 'Microsoft'}
    #     response = self.client.post(url, data=data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Customer.objects.get(company_name='Microsoft'))

class TestCustomer(APITestCase):
    
    url = reverse_lazy('customers-list')
    print("URL", url)
    sales_user = MyUser.objects.create_user(email='testsalesuser@epicevents.com', password='admin1234')
        
    def test_create_existing_customers(self):
        force_authenticate(user=self.sales_user)
        new_customer = Customer.objects.create(company_name='Microsoft', email='contact@microsoft.com', sales_contact=self.sales_user)
        response = self.client.get(self.url)
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        