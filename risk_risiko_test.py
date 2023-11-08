from pytest_mock import MockerFixture
import risk_risiko

def test_compare() -> None:
    assert risk_risiko.compare(4,5) == "blue"
    assert risk_risiko.compare(5,5) == "blue"
    assert risk_risiko.compare(6,5) == "red"
    