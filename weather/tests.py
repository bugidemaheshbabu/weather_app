from django.test import TestCase
from weather.models import City

# Create your tests here.
print("Running tests")

class CityTestCase(TestCase):
    def setUp(self):
        City.objects.create(name="Kolkata")
        City.objects.create(name="Kadapa")
    
    def test_city_names(self):
        city_1 = City.objects.get(name="Kolkata")
        city_2 = City.objects.get(name="Kadapa")

        self.assertEqual(city_1.name, 'Kolkata')
        self.assertEqual(city_2.name, 'Kadapa')
