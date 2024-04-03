from django.test import TransactionTestCase, Client
from ..models import Course
from django.urls import reverse
from ..forms import NewCourseForm
from django.contrib.auth import get_user_model

User = get_user_model()


class NewCourseFormTest(TransactionTestCase):

    def setUp(self):
        # Unauthorized client
        self.guest_client = Client()
        # Create user
        self.user = User.objects.create_user(username='HasNoName')
        # Authorized client
        self.authorized_client = Client()
        # Authorize user
        self.authorized_client.force_login(self.user)

    def test_form_is_valid(self):
        form_data = {
            'course_name': 'TestCourse',
            'course_date_begin': '20.04.2024',
            'course_time_begin': '08:00',
            'course_location': 'TestLocation',
            'course_tutor': 'TestTutor',
            'course_date_end': '21.04.2024',
            'course_time_end': '17:00',
            'course_status': 'Запланирован'
        }

        form = NewCourseForm(data=form_data)
        response = self.authorized_client.post(reverse('new_course'), form_data)
        self.assertTrue(form.is_valid())
        self.assertRedirects(response, reverse('all_courses'))
