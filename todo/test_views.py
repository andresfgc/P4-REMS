from django.test import TestCase
from .models import Property


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_add_property_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_property.html')

    def test_edit_property_page(self):
        property = Property.objects.create(property_number='Tower 2, Apartment 1805', Price='145000', Status='Available')  #needs to be reviewed with mentor
        response = self.client.get(f'/edit/{property.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_property.html')

    def test_can_add_property(self):
        response = self.client.post('/add', {'property_number':'Tower 2, Apartment 1805', 'Price':'145000', 'Status':'Available'})  #needs to be reviewed with mentor
        self.assertRedirects(response, '/')

    def test_can_delete_property(self):
        property = Property.objects.create(property_number='Tower 2, Apartment 1805', Price='145000', Status='Available')  #needs to be reviewed with mentor
        response = self.client.get(f'/delete/{property.id}')
        self.assertRedirects(response, '/')
        existing_items = Property.objects.filter(id=property.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_edit_property(self):
        property = Property.objects.create(property_number='Test property')  #needs to be reviewed with mentor
        response = self.client.post(f'/edit/{property.id}', {'name': 'Updated property'})
        self.assertRedirects(response, '/')
        existing_items = Property.objects.get(id=property.id)
        self.assertEqual(updated_property.name, 'Updated property')