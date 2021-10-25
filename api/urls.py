from business import views as api_view
from django.urls import path

urlpatterns = [
    path('customers/', api_view.CustomerApiView.as_view(), name='customers'),
    path('customers/<int:pk>/', api_view.CustomerApiDtailView.as_view(), name='customer-detail'),
]
