from business import views as api_view
from django.urls import path

urlpatterns = [
    path('customers/', api_view.CustomerApiView.as_view(), name='customers'),
]
