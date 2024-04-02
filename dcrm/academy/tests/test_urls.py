from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from ..models import Course, Attendee

User = get_user_model()


class AuthorizedUserUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        course = Course.objects.create(
            course_name='TestCourse',
            course_date_begin='2024-04-20',
            course_time_begin='08:00',
            course_location='TestLocation',
            course_tutor='TestTutor',
            course_date_end='2024-04-21',
            course_time_end='17:00',
            course_status='TestStatus'
        )

        Attendee.objects.create(
            attendee_course_id=course,
            attendee_last_name_rus='ТестФамилия',
            attendee_first_name_rus='ТестИмя',
            attendee_fathers_name_rus='ТестОтчество',
            attendee_last_name_eng='TestSurname',
            attendee_first_name_eng='TestName',
            attendee_email='TestEmail@mail.com',
            attendee_phone='+7-999-123-4567',
            attendee_company='TestCompany',
            attendee_position='TestPosition',
            attendee_contract_number='TestContractNumber',
            attendee_contract_status='TestContractStatus',
            attendee_invoice_status='TestInvoiceStatus',
            attendee_course_price='1000 TestPrice'
        )

    def setUp(self):
        # Unauthorized client
        self.guest_client = Client()
        # Create user
        self.user = User.objects.create_user(username='HasNoName')
        # Authorized client
        self.authorized_client = Client()
        # Authorize user
        self.authorized_client.force_login(self.user)

        # Availability of pages to authorized user and redirect unauth

        # Course urls

    def test_new_course_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/new-course/')
        self.assertEqual(response.status_code, 200)

    def test_new_course_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/new-course/')
        self.assertRedirects(response, '/')

    def test_all_courses_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/all-courses/')
        self.assertEqual(response.status_code, 200)

    def test_all_courses_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/all-courses/')
        self.assertRedirects(response, '/')

    def test_update_course_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/update-course/1')
        self.assertEqual(response.status_code, 200)

    def test_update_course_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/update-course/1')
        self.assertRedirects(response, '/')

    def test_delete_course_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/delete-course/1')
        self.assertRedirects(response, '/')

    def test_delete_course_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/delete-course/1')
        self.assertRedirects(response, '/')

    def test_course_attendees_all_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/course-attendees-all/1')
        self.assertEqual(response.status_code, 200)

    def test_course_attendees_all_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/course-attendees-all/1')
        self.assertRedirects(response, '/')

        # Attendee urls

    def test_attendees_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/attendees/')
        self.assertEqual(response.status_code, 200)

    def test_attendees_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/attendees/')
        self.assertRedirects(response, '/')

    def test_delete_attendee_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/delete-attendee/1')
        self.assertRedirects(response, '/course-attendees-all/1')

    def test_delete_attendee_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/delete-attendee/1')
        self.assertRedirects(response, '/')

    def test_update_attendee_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/update-attendee/1')
        self.assertEqual(response.status_code, 200)

    def test_update_attendee_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/update-attendee/1')
        self.assertRedirects(response, '/')

    def test_add_attendee_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/course-attendees-all/1/add-attendee/')
        self.assertEqual(response.status_code, 200)

    def test_add_attendee_url_redirect_anonymous_user(self):
        response = self.guest_client.get('/course-attendees-all/1/add-attendee/')
        self.assertRedirects(response, '/')

    # Template tests:

        # Without kwargs

    def test_urls_use_correct_templates(self):
        templates_url_names = {
            'all_courses.html': '/all-courses/',
            'attendees.html': '/attendees/',
            'new_course.html': '/new-course/',
        }
        for template, address in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)

        # With kwargs

    def test_url_template_update_course(self):
        url = reverse('update_course', kwargs={'pk': 1})
        response = self.authorized_client.get(url)
        self.assertTemplateUsed(response, 'update_course.html')

    def test_url_template_update_attendee(self):
        url = reverse('update_attendee', kwargs={'pk': 1})
        response = self.authorized_client.get(url)
        self.assertTemplateUsed(response, 'update_attendee.html')

    def test_url_template_course_attendees_all(self):
        url = reverse('course_attendees_all', kwargs={'course_id': 1})
        response = self.authorized_client.get(url)
        self.assertTemplateUsed(response, 'course_attendees_all.html')

    def test_url_template_add_attendee(self):
        url = reverse('add_attendee', kwargs={'course_id': 1})
        response = self.authorized_client.get(url)
        self.assertTemplateUsed(response, 'add_attendee.html')
