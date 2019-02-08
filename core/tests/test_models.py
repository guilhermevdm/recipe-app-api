from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test if creating a new user with email is successful
        """

        email = 'test@gambs.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        """
        Test if email for a new user is normalized
        """

        email = 'test@GaMbS.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with invalid email raises error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpassword123')

    def test_create_super_user(self):
        """
        Test if new superuser is actually a superuser
        """

        email = 'test@gambs.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
