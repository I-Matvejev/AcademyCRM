from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from ..views import home
from ..models import Course, Attendee

User = get_user_model()


class AuthorizedUserUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Course.objects.create(
            course_name='Test course',
            course_date_begin='2024-04-20',
            course_time_begin='08:00',
            course_location='TestLocation',
            course_tutor='TestTutor',
            course_date_end='2024-04-21',
            course_time_end='17:00',
            course_status='TestStatus'
        )

    def setUp(self):
        # Создаем неавторизованного клиента
        self.guest_client = Client()
        # Создаем пользователя
        self.user = User.objects.create_user(username='HasNoName')
        # Создаем авторизованного клиента
        self.authorized_client = Client()
        # Авторизуем пользователя
        self.authorized_client.force_login(self.user)

        # Проверяем доступность страниц для авторизованного пользователя

    def test_new_course_url_exists_at_desired_location(self):
        """Страница /new-course/ доступна авторизованному пользователю."""
        response = self.authorized_client.get('/new-course/')
        self.assertEqual(response.status_code, 200)

    def test_new_course_url_redirect_anonymous_user(self):
        """Страница /new-course/ перенаправляет неавторизованного пользователя."""
        response = self.guest_client.get('/new-course/')
        self.assertRedirects(response, '/')

    def test_urls_use_correct_templates(self):
        """URL-адрес использует соответствующий шаблон."""
        # Шаблоны по адресам
        templates_url_names = {
            # 'add_attendee.html': '/course-attendees-all/<int:course_id>/add-attendee/',
            'all_courses.html': '/all-courses/',
            'attendees.html': '/attendees/',
            # 'course_attendees_all.html': '/course-attendees-all/<int:course_id>/',
            'new_course.html': '/new-course/',
            # 'update_attendee.html': '/update-attendee/<int:pk>/',
            # 'update_course.html': '/update-course/<int:pk>/',
        }
        for template, address in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)

    def test_url_with_para(self):
        url = reverse('update_course', kwargs={'pk': 1})
        response = self.authorized_client.get(url)
        self.assertTemplateUsed(response, 'update_course.html')
