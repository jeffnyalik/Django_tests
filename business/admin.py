from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['title', 'fullName', 'gender', 'createdBy', 'created', 'status']
    readonly_fields = ['created']

admin.register(Customer, CustomerAdmin)