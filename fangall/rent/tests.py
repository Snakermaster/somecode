from django.test import TestCase


class TestViews(TestCase):

    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(200, resp.status_code)
