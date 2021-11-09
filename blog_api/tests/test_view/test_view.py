from django.test.testcases import TestCase, Client


class ViewsTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_res(self):
        self.assertEqual(self.c.get('/').status_code, 200)
