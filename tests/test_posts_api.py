import pytest

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


def test_update_post_put():
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_update_post_patch():
    payload = {
        "title": "patched title"
    }

    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == payload["title"]
    assert "id" in data
    assert "body" in data
    assert "userId" in data


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200


def test_get_posts_by_user_id():
    params = {
        "userId": 1
    }

    response = requests.get(f"{BASE_URL}/posts", params=params)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for post in data:
        assert post["userId"] == params["userId"]


def test_get_posts_by_user_id():
    params = {
        "userId": 1
    }

    response = requests.get(f"{BASE_URL}/posts", params=params)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for post in data:
        assert post["userId"] == params["userId"]


def test_get_posts_by_unknown_user_id():
    params = {
        "userId": 999999
    }

    response = requests.get(f"{BASE_URL}/posts", params=params)

    assert response.status_code == 200

    data = response.json()

    assert data == []


def test_get_post_with_accept_json_header():
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(f"{BASE_URL}/posts/1", headers=headers)

    assert response.status_code == 200

    assert "application/json" in response.headers["Content-Type"]


def test_get_post_response_content_type():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    assert "application/json" in response.headers["Content-Type"]


@pytest.mark.parametrize("payload", [
    {},
    {"title": "only title"},
    {"body": "only body"},
    {"userId": 1},
])
def test_create_post_with_incomplete_payload(payload):
    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
