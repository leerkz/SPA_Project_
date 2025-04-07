from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Course, Lesson, Subscription

User = get_user_model()

class CourseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Test Course")

    def test_create_lesson_with_youtube_link(self):
        response = self.client.post('/lessons/', {'title': 'Lesson 1', 'link': 'https://youtube.com/video123'})
        self.assertEqual(response.status_code, 201)

    def test_create_lesson_with_bad_link(self):
        response = self.client.post('/lessons/', {'title': 'Lesson 1', 'link': 'https://badsite.com/video'})
        self.assertEqual(response.status_code, 400)

    def test_subscribe_and_unsubscribe(self):
        response = self.client.post('/subscribe/', {'course_id': self.course.id})
        self.assertEqual(response.data['message'], 'Подписка добавлена')

        response = self.client.post('/subscribe/', {'course_id': self.course.id})
        self.assertEqual(response.data['message'], 'Подписка удалена')
