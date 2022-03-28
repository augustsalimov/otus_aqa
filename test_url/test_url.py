import requests


def test_url(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(status_code), \
        f"Expected status code: {status_code}. Instead: {response.status_code}"
