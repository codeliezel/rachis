from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rachis.apps.authentication.models import User

class UserTest(APITestCase):
    def test_create_new_user_201(self):
        """
        test to create a new user
        """
        url = reverse('auth:user_sign_up')
        data = {'full_names': 'ade ade', 'username': 'lallala', 'email': 'cft@net.co',
        'password': 'hdhhdd87u' }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1) 
