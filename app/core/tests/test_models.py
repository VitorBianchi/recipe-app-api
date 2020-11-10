from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Testando se o usuario foi criado com o email """
        email = 'vitor@maquinaweb.com.br'
        password = 'Teste@12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Testando a normalização dos emails """
        email = 'test@BIANCHI.COM'
        user = get_user_model().objects.create_user(email, '@Teste123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Testando aviso de erro caso nao tenha email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Testando a criação de um superuser """
        user = get_user_model().objects.create_superuser(
            'test@bianchi.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
