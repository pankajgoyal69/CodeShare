from test_plus.test import TestCase
from app_code_share.models import CodeShare
<<<<<<< HEAD
import random


class CodeShareTests(TestCase):

    def setUp(self):
        self.code_share = 'testcode'
        self.a = random.randrange(0, 6)
        self.hash_value = str(hash(self.code_share))[self.a:self.a + 8]
=======
from django.utils.crypto import get_random_string


class TestCodeShare(TestCase):

    def setUp(self):
        self.code_share = 'testcode'
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.hash_value = get_random_string(8, self.chars)
>>>>>>> 241842cb9400a3562e848e9d76455a730741dead
        self.file_name = 'testfilename'

        CodeShare.objects.create(
            code=self.code_share,
            hash_value=self.hash_value,
            file_name=self.file_name
        )

    def test_post_list(self):
        response = self.client.get('/app/' + self.hash_value + '/')
        self.assertEqual(response.status_code, 200)
