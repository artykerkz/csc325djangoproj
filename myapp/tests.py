from django.test import SimpleTestCase
from django.urls import reverse


class HomeViewTests(SimpleTestCase):
    def test_home_page_returns_success(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_welcome_message(self):
        response = self.client.get(reverse("home"))

        self.assertContains(response, "Hello, World!")


class AboutViewTests(SimpleTestCase):
    def test_about_page_returns_success(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)

    def test_about_page_contains_heading_and_description(self):
        response = self.client.get(reverse("about"))

        self.assertContains(response, "About Page")
        self.assertContains(response, "about page of my Django application")

class ApiHomeViewTests(SimpleTestCase):
    def test_api_home_page_returns_success(self):
        response = self.client.get(reverse("api_home"))

        self.assertEqual(response.status_code, 200)

    def test_api_home_page_contains_message(self):
        response = self.client.get(reverse("api_home"))

        self.assertContains(response, "Hello, World! This is the API home endpoint.")
        self.assertEqual(response.json()["status"], "success")

    