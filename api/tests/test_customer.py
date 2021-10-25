from django.test import SimpleTestCase
from django.urls import resolve, reverse
from business.views import CustomerApiView
from rest_framework.test import APITestCase
from rest_framework import status

class ApIUrlsTest(SimpleTestCase):
    def test_get_customers_is_resolved(self):
        url = reverse('customers')
        self.assertEquals(resolve(url).func.view_class, CustomerApiView)
    
class ApICustomerTest(APITestCase):
    def test_get_customer_api(self):
        url = reverse('customers')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_custor_not_found(self):
        url = reverse('customers')
        response = self.client.get(url)
        self.assertNotEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_customer_api(self):
        data = {'createdBy': '1','name': 'krishna', 'title': 'Mr', 'fullName': 'Krishna programming', 'gender': 'M'}
        url = reverse('customers')
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_customer_api(self):
        data = {'createdBy': '1','name': 'krishna', 'title': 'Mr', 'fullName': 'Krishna programming', 'gender': 'M'}
        url = reverse('customers')
        response = self.client.post(url, data, format='json')
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
    


        
