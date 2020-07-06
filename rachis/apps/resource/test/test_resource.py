from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rachis.apps.resource.models import Resource

class ResourceTest(APITestCase):
    def test_create_resource_201(self):
        """
        create a new resource object
        """
        url = reverse('resource')
        data = {'title': 'DabApps', 'description': 'la la amaa', 'author': 'funmiff', 
        'tags': '["deee", "eeee"]', 'link': 'https://github.com/' }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Resource.objects.count(), 1)
       
    def test_create_resource_400(self):
        """
        returns an error when creating a new resource object
        """
        url = reverse('resource')
        data = {'description': 'la la amaa', 'author': 'funmiff', 
        'tags': '["deee", "eeee"]', 'link': 'https://github.com/' }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_resources_200(self):
        """
        get all resources
        """
        url = reverse('resource')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 