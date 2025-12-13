from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project

class ProjectAPITests(APITestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            slug='test-project',
            short_description='A short description',
            content='Some content'
        )

    def test_list_projects(self):
        """
        Ensure we can list all projects.
        """
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.project.title)

    def test_retrieve_project(self):
        """
        Ensure we can retrieve a single project by slug.
        """
        url = reverse('project-detail', kwargs={'slug': self.project.slug})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.project.title)