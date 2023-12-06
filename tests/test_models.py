from django.test import TestCase
from FinalApp.models import Menu, Booking


class MenuTest(TestCase):
    def test_menu(self):
       item = Menu.objects.create(Title='Ice Cream', Price=2, Inventory=100)
       self.assertEqual(item.Title, 'Ice Cream')