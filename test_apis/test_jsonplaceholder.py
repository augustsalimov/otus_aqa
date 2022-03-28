import requests
import pytest
# print(response.json())


class TestJson:
    update_post = [
        ("algebra", "Algebra is the study of math symbols and the rules for manipulating these symbols in formulas"),
        ("topology", "Topology is about a geometric object that are preserved under continuous deformations,")
    ]
    update_users = [
        ("Rene Descartes", "rene"),
        ("Leonhard Euler", "leo")
    ]

    def setup(self):
        self.url = 'https://jsonplaceholder.typicode.com'

    def test_posts(self):
        response = requests.get(f"{self.url}/posts/1")
        assert response.status_code == 200

    @pytest.mark.parametrize("title, body", update_post)
    def test_update_post(self, title, body):
        data = {
            'title': title,
            'body': body,
            'userId': 1
        }
        response = requests.put(f"{self.url}/posts/1", data=data)
        assert response.status_code == 200

    def test_users(self):
        response = requests.get(f"{self.url}/users")
        assert response.status_code == 200

    @pytest.mark.parametrize("name, nickname", update_users)
    def test_update_users(self, name, nickname):
        data = {
            'name': name,
            'username': nickname
        }
        response = requests.put(f"{self.url}/users/1", data=data)
        assert response.status_code == 200

    def test_photos(self):
        response = requests.get(f"{self.url}/photos")
        assert response.status_code == 200
