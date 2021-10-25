from rest_framework import serializers
from business.models import Customer


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        