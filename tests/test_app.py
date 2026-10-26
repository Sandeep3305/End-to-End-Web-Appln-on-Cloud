import unittest

from app import app


class PortfolioAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_main_pages_load(self):
        pages = [
            "/",
            "/about",
            "/experience",
            "/projects",
            "/skills",
            "/education",
            "/contact",
        ]

        for page in pages:
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertEqual(response.status_code, 200)

    def test_health_endpoint_reports_healthy(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})


if __name__ == "__main__":
    unittest.main()
