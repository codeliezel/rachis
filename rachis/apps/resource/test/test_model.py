from django.test import TestCase
from rachis.apps.resource.models import Resource
from django.utils import timezone
from django.urls import reverse

# models test
class ResourceTest(TestCase):

    def create_resource(self, title="DabApps", description="la la amaa",
        author="funmiff", link="https://github.com/"):
        return Resource.objects.create(title=title, description=description,
        author=author, link=link)

    def test_resource_model(self):
        w = self.create_resource()
        self.assertTrue(isinstance(w, Resource))
        self.assertEqual(w.__str__(), w.title)