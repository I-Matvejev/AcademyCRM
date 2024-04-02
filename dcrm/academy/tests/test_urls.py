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
        course = Course.objects.create(
            course_name='Test course',
            course_date_begin='2024-04-20',
            course_time_begin='08:00',
            course_location='TestLocation',
            course_tutor='TestTutor',
            course_date_end='2024-04-21',
            course_time_end='17:00',
            course_status='TestStatus'
        )
    # @classmethod
    # def setUpClassAttendee(cls):
    #     super().setUpClass()
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

        # Availability of pages to authorized user

    def test_new_course_url_exists_at_desired_location(self):
        """Page /new-course/ is available to auth user"""
        response = self.authorized_client.get('/new-course/')
        self.assertEqual(response.status_code, 200)

    def test_new_course_url_redirect_anonymous_user(self):
        """Page /new-course/ redirects unauth user."""
        response = self.guest_client.get('/new-course/')
        self.assertRedirects(response, '/')

    def test_urls_use_correct_templates(self):
        """URL use correct templates. Without kwargs"""
        templates_url_names = {
            # 'add_attendee.html': '/course-attendees-all/<int:course_id>/add-attendee/',
            'all_courses.html': '/all-courses/',
            'attendees.html': '/attendees/',
            # 'course_attendees_all.html': '/course-attendees-all/<int:course_id>/',
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
