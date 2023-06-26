from django.test import TestCase
from .forms import PropertyForm


class TestPropertyForm(TestCase):

    def test_property_number_is_required(self):
        form = PropertyForm({'property_number':''})
        self.assertFalse(form.is_valid())
        self.assertIn('property_number', form.errors.keys())
        self.assertEqual(form.errors['property_number'][0], 'This field is required.')

    def test_Price_is_required(self):
        form = PropertyForm({'Price':''})
        self.assertFalse(form.is_valid())
        self.assertIn('Price', form.errors.keys())
        self.assertEqual(form.errors['Price'][0], 'This field is required.')
    
    def test_Status_is_required(self):
        form = PropertyForm({'Status':''})
        self.assertFalse(form.is_valid())
        self.assertIn('Status', form.errors.keys())
        self.assertEqual(form.errors['Status'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(Self):
        form = PropertyForm()
        self.assertEqual(form.Meta.fields, ['property_number', 'Price', 'Status'])

        

