from django.test import TestCase, Client
from django.urls import resolve


# Create your tests here.
class AppTest(TestCase):
    def test1(self):
        response_html = Client().get('/mywatchlist/html/')
        self.assertEqual(response_html.status_code,200)
    def test2(self):
        response_xml = Client().get('/mywatchlist/xml/')
        self.assertEqual(response_xml.status_code,200)
    def test3(self):
        response_json = Client().get('/mywatchlist/json/')
        self.assertEqual(response_json.status_code,200)
# Create your tests here.
