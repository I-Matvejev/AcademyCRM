from django.test import TransactionTestCase, Client
from ..models import Course, Attendee
from django.urls import reverse
from ..forms import NewCourseForm, CourseAttendeesForm
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

    def test_form_is_valid_new_course(self):
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

    def test_form_is_valid_update_course(self):

        existing_course = Course.objects.create(
            course_name='TestCourse',
            course_date_begin='2024-04-20',
            course_time_begin='08:00',
            course_location='TestLocation',
            course_tutor='TestTutor',
            course_date_end='2024-04-21',
            course_time_end='17:00',
            course_status='TestStatus'
        )

        form_data = {
            'course_name': 'TestCourse1',
            'course_date_begin': '20.04.2024',
            'course_time_begin': '08:00',
            'course_location': 'TestLocation',
            'course_tutor': 'TestTutor',
            'course_date_end': '21.04.2024',
            'course_time_end': '17:00',
            'course_status': 'Запланирован'
        }

        self.assertTrue(existing_course)
        self.assertEqual(existing_course.course_name, 'TestCourse')

        form = NewCourseForm(instance=existing_course, data=form_data)
        response = self.authorized_client.post(reverse('update_course', kwargs={'pk': existing_course.id}), form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(existing_course.course_name, 'TestCourse1')
        self.assertRedirects(response, reverse('all_courses'))

    def test_form_is_valid_add_attendee(self):

        course_test_attendee = Course.objects.create(
            course_name='TestCourse',
            course_date_begin='2024-04-20',
            course_time_begin='08:00',
            course_location='TestLocation',
            course_tutor='TestTutor',
            course_date_end='2024-04-21',
            course_time_end='17:00',
            course_status='TestStatus'
        )

        form_data_attendee = {
            'attendee_course_id': course_test_attendee.id,
            'attendee_last_name_rus': 'Тестфамилия',
            'attendee_first_name_rus': 'Тестимя',
            'attendee_fathers_name_rus': 'Тестотчество',
            'attendee_last_name_eng': 'Testsurname',
            'attendee_first_name_eng': 'Testname',
            'attendee_email': 'TestEmail@mail.com',
            'attendee_phone': '+79991234567',
            'attendee_company': 'TestCompany',
            'attendee_position': 'TestPosition',
            'attendee_contract_number': 'TestContractNumber',
            'attendee_contract_status': 'Подписан',
            'attendee_invoice_status': 'Оплачен',
            'attendee_course_price': '1000',
            'attendee_contact_last_name_rus': 'Тестфамилияконтакт',
            'attendee_contact_first_name_rus': 'Тестимяконтакт',
            'attendee_contact_fathers_name_rus': 'Тестотчествоконтакт',
            'attendee_contact_email': 'TestMailContact@mail.com',
            'attendee_contact_phone': '+7123456789',
            'attendee_contact_position': 'TestPositionContact'
        }

        form = CourseAttendeesForm(data=form_data_attendee)
        response = self.authorized_client.post(reverse('add_attendee', kwargs={'course_id': course_test_attendee.id}), form_data_attendee)
        self.assertTrue(form.is_valid())
        self.assertRedirects(response, reverse('course_attendees_all', kwargs={'course_id': course_test_attendee.id}))

    def test_form_is_valid_update_attendee(self):

        course_test_attendee = Course.objects.create(
            course_name='TestCourse',
            course_date_begin='2024-04-20',
            course_time_begin='08:00',
            course_location='TestLocation',
            course_tutor='TestTutor',
            course_date_end='2024-04-21',
            course_time_end='17:00',
            course_status='TestStatus'
        )

        test_attendee = Attendee.objects.create(
            attendee_course_id=course_test_attendee,
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

        form_data_attendee = {
            'attendee_course_id': course_test_attendee.id,
            'attendee_last_name_rus': 'Тестфамилияизменилась',
            'attendee_first_name_rus': 'Тестимя',
            'attendee_fathers_name_rus': 'Тестотчество',
            'attendee_last_name_eng': 'Testsurname',
            'attendee_first_name_eng': 'Testname',
            'attendee_email': 'TestEmail@mail.com',
            'attendee_phone': '+79991234567',
            'attendee_company': 'TestCompany',
            'attendee_position': 'TestPosition',
            'attendee_contract_number': 'TestContractNumber',
            'attendee_contract_status': 'Подписан',
            'attendee_invoice_status': 'Оплачен',
            'attendee_course_price': '1000',
            'attendee_contact_last_name_rus': 'Тестфамилияконтакт',
            'attendee_contact_first_name_rus': 'Тестимяконтакт',
            'attendee_contact_fathers_name_rus': 'Тестотчествоконтакт',
            'attendee_contact_email': 'TestMailContact@mail.com',
            'attendee_contact_phone': '+7123456789',
            'attendee_contact_position': 'TestPositionContact'
        }

        form = CourseAttendeesForm(instance=test_attendee, data=form_data_attendee)
        response = self.authorized_client.post(reverse('update_attendee', kwargs={'pk': test_attendee.id}), form_data_attendee)
        self.assertTrue(form.is_valid())
        self.assertEqual(test_attendee.attendee_last_name_rus, 'Тестфамилияизменилась')
        self.assertRedirects(response, reverse('course_attendees_all', kwargs={'course_id': course_test_attendee.id}))
