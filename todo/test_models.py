from django.test import TestCase
from .models import Property


class TestModels(TestCase):

    def test_property_string_method_returns_name(self):
        property = Property.objects.create(property_number='Tower 2, Apartment 1805')  #need to be reviewed with mentor
        self.assertEqual(str(item), 'Tower 2, Apartment 1805')
