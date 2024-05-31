import pytest 
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/YermakAleksandr")
    body = r.json()
    headers = r.headers

    assert body["name"] == None
    assert r.status_code == 200
    assert headers["Server"] == "GitHub.com"


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/adsdssvdhgdsvyv")

    assert r.status_code == 404