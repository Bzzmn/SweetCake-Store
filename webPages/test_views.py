# from django.test import TestCase
# Create your tests here.

from django.test import TestCase
from webPages.models import Torta, Cupcake

class TortaModelTest(TestCase):
    def setUp(self):
        self.torta = Torta.objects.create(
            name="Test Torta",
            description="This is a test torta",
            price=10.00,
            is_private=False,
            is_featured=True
        )

    def test_torta_name(self):
        self.assertEqual(self.torta.name, "Test Torta") 

    def test_torta_description(self):
        self.assertEqual(self.torta.description, "This is a test torta")

    def test_torta_price(self):
        self.assertEqual(self.torta.price, 10.00)

    def test_torta_is_private(self):
        self.assertEqual(self.torta.is_private, False)


