from django.test import TestCase
from django.utils import unittest
from django.test.client import RequestFactory


# Create your tests here.
class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test1(self):
        # Create an instance of a GET request.
        request = self.factory.get('https://reqres.in/api/users/2')

        response = getrequest(request)
        self.assertEqual(response.status_code, 200)
     
    def test2(self):
        request = self.factory.get('https://reqres.in/api/users')

        response = postrequest(request)
        self.assertEqual(response.status_code, 200)

