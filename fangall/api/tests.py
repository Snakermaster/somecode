from django.test import TestCase


class TestApi(TestCase):

    def test_provinces(self):
        resp = self.client.get('/api/districts/')
        self.assertEqual(200, resp.status_code)

    def test_districts(self):
        pass

    def test_agents(self):
        resp = self.client.get('/api/agents/1')
        self.assertEqual(200, resp.status_code)

    def test_estates(self):
        pass

    def test_housetype(self):
        resp = self.client.delete('/api/housetype/8')
        self.assertEqual(404, resp.status_code)
