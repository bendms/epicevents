from django.urls import include, path
from rest_framework_nested import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'customers', views.CustomerViewSet)
# router.register(r'contracts', views.ContractViewSet)
# router.register(r'events', views.EventViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
# /customers/
# /customers/{pk}/

customer_router = routers.NestedSimpleRouter(router, r'customers', lookup='customer')
customer_router.register(r'contracts', views.ContractViewSet, basename='contracts')
# /customers/{pk}/contracts/
# /customers/{pk}/contracts/{pk}/

contract_router = routers.NestedSimpleRouter(customer_router, r'contracts', lookup='contract')
contract_router.register(r'events', views.EventViewSet, basename='events')
# /customers/{pk}/contracts/{pk}/events/
# /customers/{pk}/contracts/{pk}/events/{pk}/

urlpatterns = [
    path('', include(router.urls)),
    path('', include(customer_router.urls)),
    path('', include(contract_router.urls)),
]
