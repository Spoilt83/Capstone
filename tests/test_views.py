from django.test import TestCase
from FinalApp.models import Menu, Booking
from django.urls import reverse

class MenuTestViews(TestCase):
    
    def setUp(self):
        Menu.objects.create(Title='Pizza', Price=6.5, Inventory=10)
        
    def test_get_all(self):
        # Retrieve all Menu objects
        url = reverse('http://127.0.0.1:8000/restaurant/menu/')
        response = self.client.get(url)
        
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        
        