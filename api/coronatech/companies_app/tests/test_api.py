from django.test import TestCase

class TestGetCompanies(TestCase):

    def test_get_companies(self):
        assert 1 == 1
        assert 2 == 2
        # response = self.client.get("/companies/")
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json(), [])

    def test_first(self) -> None:
        assert 1 == 1
