import json
import pytest

from django.urls import reverse
from api.coronatech.companies_app.models import Company
import datetime

d = datetime.date(2010, 10, 22)
companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db



def test_zero_companies_should_return_zero_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert response.json() == []

def test_one_companies_exist(client) -> None:
    cmy = Company.objects.create(name="Baidu", last_updated=d)
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]

    assert response.status_code == 200
    assert response_content.get("name") == cmy.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("last_updated") == "2010-10-22"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""

def test_companies_without_arguments_should_fail(client) -> None:
    response = client.post(companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}

def test_create_existing_company_should_fail(client) -> None:
    Company.objects.create(name="apple")
    response = client.post(companies_url, data={"name": "apple"})
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["company with this name already exists."]}

def test_create_company_with_only_name_all_fields_should_be_default(client) -> None:
    response = client.post(path=companies_url, data={"name": "some_cmy_name"})  # path keyword optional
    assert response.status_code == 201
    response_content = json.loads(response.content)

    assert response_content.get("name") == "some_cmy_name"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("last_updated") == None
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""

def test_create_companies_with_layoff_status_should_succeed(client) -> None:
    response = client.post(
        companies_url, data={"name": "some_cmy", "status": "Layoff"}
    )
    assert response.status_code == 201

def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(
        companies_url,
        data={"name": "some_cmy", "status": "wrong_status_not_in_status_choice"},
    )
    assert response.status_code == 400
    assert "wrong_status_not_in_status_choice" in str(response.content)


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
