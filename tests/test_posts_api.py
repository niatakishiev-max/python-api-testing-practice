import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)


def test_get_posts_list():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_post = data[0]

    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post


def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/999999")

    assert response.status_code == 404


def test_create_post():
    payload = {
        "title": "test title",
        "body": "test body",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
