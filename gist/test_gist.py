import pytest


def test_first() -> None:
    assert 1 == 1


@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2


@pytest.mark.skipif(4 > 1, reason="checking given condition")
def test_shouldbe_skipif() -> None:
    assert 1 == 2


@pytest.mark.xfail
def test_should_notcare_about_fail() -> None:
    assert 3 == 3


class Company:
    def __init__(self, name: str, stock_symbol: str) -> None:
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self) -> str:
        return f"{self.name}: {self.stock_symbol}"


@pytest.fixture
def company() -> Company:
    return Company("Google", "GOOG")


def test_company(company: Company) -> None:
    print(f"printing {company} from fixture")


# pytest fixture: Pytest fixtures are functions that can be used to manage our apps states and dependencies.
#  Most of the time, we use fixtures to create objects that we can use in our tests.


@pytest.mark.parametrize("company_name", ["Google", "Apple", "Microsoft"])
def test_my_company_name(company_name: str) -> None:
    print(f"It is  {company_name} ")
