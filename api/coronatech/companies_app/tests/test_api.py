import json

import pytest

from django.test import TestCase
# from unittest import TestCase
from django.test import Client
from django.urls import reverse
from api.coronatech.companies_app.models import Company
import datetime

d = datetime.date(2010, 10, 22)


# companies_url = reverse("companies-list")
# client = Client()


# @pytest.mark.django_db   #this marking only needed when not using native django TestCase
class TestGetCompanies(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def tearDown(self) -> None:
        pass

    def test_zero_companies_should_return_zero_empty_list(self) -> None:
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
        print("hello")

    def test_one_companies_exist(self) -> None:
        cmy = Company.objects.create(name="Baidu", last_updated=d)
        # cmy.last_updated("last_updated"=d)
        response = self.client.get(self.companies_url)
        response_content = json.loads(response.content)[0]
        print(response_content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), cmy.name)
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("last_updated"), "2010-10-22")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")

    def test_companies_without_arguments_should_fail(self) -> None:
        response = self.client.post(self.companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content), {"name": ["This field is required."]}
        )

    def test_create_existing_company_should_fail(self) -> None:
        Company.objects.create(name="apple")
        response = self.client.post(self.companies_url, data={"name": "apple"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content),
            {"name": ["company with this name already exists."]},
        )

    def test_create_company_with_only_name_all_fields_should_be_default(self) -> None:
        response = self.client.post(
            path=self.companies_url, data={"name": "some_cmy_name"}
        )  # path keyword optional
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)

        self.assertEqual(response_content.get("name"), "some_cmy_name")
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("last_updated"), None)
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")

    def test_create_companies_with_layoff_status_should_succeed(self) -> None:
        response = self.client.post(
            self.companies_url, data={"name": "some_cmy", "status": "Layoff"}
        )
        self.assertEqual(response.status_code, 201)

    def test_create_company_with_wrong_status_should_fail(self) -> None:
        response = self.client.post(
            self.companies_url,
            data={"name": "some_cmy", "status": "wrong_status_not_in_status_choice"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("wrong_status_not_in_status_choice", str(response.content))


@pytest.mark.xfail
def test_should_be_ok_if_fail() -> None:
    assert 1 == 2


@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception example")


def test_raise_covid19_exception() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception example" == str(e.value)


import logging

logger = logging.getLogger("log related to corona")


def function_that_log_something() -> None:
    try:
        raise ValueError("Corona Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")


def test_logged_warning_level(caplog) -> None:
    # caplog is a special fixture for logging. It captures all log
    function_that_log_something()
    assert "I am logging Corona Exception" in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text
