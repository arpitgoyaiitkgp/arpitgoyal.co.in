from django.test import SimpleTestCase


class TestHomePageView(SimpleTestCase):

    def setUp(self):
        self.admin_url = '/admin/'

        self.homepage_url = '/home/'

    def test_valid_redirect_on_get_request_for_admin_interface(self):
        response = self.client.get(self.admin_url)

        self.assertEqual(response.status_code, 302)

    def test_returns_valid_response_on_get_request_for_homepage(self):
        response = self.client.get(self.homepage_url)

        self.assertEqual(response.status_code, 200)
