from django.test import TestCase
from django.urls import reverse

from .models import Task
# Create your tests here.

def create_task(title):
    return Task.objects.create(title=title)


class Check_if_task_uploaded(TestCase):
    def test_upload(self):
        #task = create_task(title='A new title')
        response = self.client.get(reverse('base:tasks'))
        self.assertQuerysetEqual(response.context['Tasks'], [])
