from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from routine.models import Routine
from routine.serializers import RoutineCreateSerializer, RoutineListSerializer, RoutineDetailSerializer


class RoutineCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('routine:create')
        self.valid_payload = {
            'name': 'Test Routine',
            'description': 'This is a test routine',
            'days': ['MON', 'WED', 'FRI']
        }
        self.invalid_payload = {
            'name': '',
            'description': '',
            'days': []
        }

    def test_create_valid_routine(self):
        response = self.client.post(self.url, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Routine.objects.count(), 1)

    def test_create_invalid_routine(self):
        response = self.client.post(self.url, data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RoutineListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('routine:list', args=[self.user.id])
        self.routine = Routine.objects.create(
            name='Test Routine',
            description='This is a test routine',
            account=self.user,
            days=[0, 2, 4]
        )

    def test_get_routine_list(self):
        response = self.client.get(self.url, data={'today': '2023-02-23'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['name'], 'Test Routine')


class RoutineDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.routine = Routine.objects.create(
            name='Test Routine',
            description='This is a test routine',
            account=self.user,
            days=[0, 2, 4]
        )
        self.url = reverse('routine:detail', args=[self.user.id, self.routine.id])
        self.valid_payload = {
            'name': 'Updated Routine',
            'description': 'This is an updated routine',
            'days': ['TUE', 'THU', 'SAT']
        }
        self.invalid_payload = {
            'name': '',
            'description': '',
            'days': []
        }

    def test_get_valid_routine(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], 'Test Routine')

    def test_get_invalid_routine(self):
        url = reverse('routine:detail', args=[self.user.id, 999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_routine(self):
        response = self.client.put(self.url, data=self.valid_payload)