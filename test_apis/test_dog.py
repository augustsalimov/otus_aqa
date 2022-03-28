import requests
import pytest


class TestDog:
    breed = [
        ("akita"), ("husky"), ("germanshepherd")
    ]

    def setup(self):
        self.url = 'https://dog.ceo'

    def test_random_image(self):
        random = '/api/breeds/image/random'
        response = requests.get(f"{self.url}{random}")
        assert response.status_code == 200
        assert response.json()['status'] == 'success'
        assert response.json()['message'] != []

    def test_all_breeds(self):
        all_breeds = '/api/breeds/list/all'
        response = requests.get(f"{self.url}{all_breeds}")
        assert response.status_code == 200
        assert response.json()['status'] == 'success'

    @pytest.mark.parametrize("breed", breed)
    def test_breed(self, breed):
        response = requests.get(f"{self.url}/api/breed/{breed}/images/random/")
        assert response.status_code == 200
        assert response.json()['status'] == 'success'

    @pytest.mark.parametrize("breed", breed)
    def test_breed_images_array(self, breed):
        response = requests.get(f"{self.url}/api/breed/{breed}/images")
        assert response.status_code == 200
        assert response.json()['status'] == 'success'

    @pytest.mark.parametrize("breed", breed)
    def test_sub_breed(self, breed):
        response = requests.get(f"{self.url}/api/breed/{breed}/list")
        assert response.status_code == 200
        assert response.json()['status'] == 'success'
