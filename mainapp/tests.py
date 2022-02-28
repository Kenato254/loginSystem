from django.test import TestCase

from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from mainapp.models import User

class UsersManagersTests(TestCase):
    
    def test_create_user(self):
        user = User.objects.create_user(
            email='user@user.com', 
            password='testuser2022',
        )
        self.assertEqual(user.email, 'user@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)        
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(NameError):
            User.objects.create_user(email)
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='password')
    
    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email='super@user.com',
            password='testuser2022',
        )
        self.assertEqual(superuser.email, 'super@user.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_delete_user(self):
        user = User.objects.create_user(
            email='delete@user.com',
            password='testuser2022'
        )
        user.delete()
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(email='delete@user.com')

    def test_user_permission(self):
        pass
    
    def test_email_validator(self):
        for invalid in ['foo', 'foo@', 'foo@bar', 'foo@.com', 'foo.com']:
            with self.assertRaises(ValidationError, msg='"%s" did not raise ValidationError.'%invalid):
                validate_email(invalid)
            
        self.assertEqual(validate_email('foo@bar.com'), None)
        self.assertEqual(validate_email('foo.bar@bar.com'), None)
        self.assertEqual(validate_email('foo-bar@bar.com'), None)
    

