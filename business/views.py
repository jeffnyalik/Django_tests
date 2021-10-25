from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from business.models import Customer
from api.serializers.customers import CustomerSerializers
from rest_framework.response import Response
from rest_framework import status


class CustomerApiView(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.filter(status='Published')
        serializer = CustomerSerializers(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, format=None):
        serializer = CustomerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerApiDtailView(APIView):
    def get(self, request, format=None, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializers(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializers(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response({'msg': 'Customer has been deleted'}, status=status.HTTP_200_OK)

