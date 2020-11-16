from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """TEST CREATING NEW USER WITH EMAIL"""
        email = 'ajeshajaayan@mail.com'
        password = 'testPassword123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EMAIL.com'
        password = 'test@123'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_no_email_raise_error(self):
        """Test if no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_create_super_user(self):
        """Test create super user"""
        email = 'superuser@mail.com'
        password = 'test@123'
        user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
