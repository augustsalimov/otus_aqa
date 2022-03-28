import requests
import pytest


class TestBreweries:
    type = [
        ("by_city", "new_york"),
        ("by_type", "large")
    ]
    id = [
        ("alameda-island-brewing-company-alameda"),
        ("madtree-brewing-cincinnati"),
        ("faction-brewing-co-alameda")
    ]

    def setup(self):
        self.url = 'https://api.openbrewerydb.org'

    @pytest.mark.parametrize("by, key", type)
    def test_list_breweries(self, by, key):
        data = {
            by: key
        }
        response = requests.get(f"{self.url}/breweries", params=data)
        assert response.status_code == 200

    @pytest.mark.parametrize("ids", id)
    def test_breweries_by_id(self, ids):
        response = requests.get(f"{self.url}/breweries/{ids}")
        assert response.status_code == 200

    def test_search(self):
        data = {
            'query': 'dog'
        }
        response = requests.get(f"{self.url}/breweries/search", params=data)
        assert response.status_code == 200

    def test_search_2(self):
        data = {
            'query': 'california'
        }
        response = requests.get(f"{self.url}/breweries/search", params=data)
        assert response.status_code == 200

    def test_autocomplete(self):
        data = {
            'query': 'boss'
        }
        response = requests.get(f"{self.url}/breweries/autocomplete", params=data)
        assert response.status_code == 200
