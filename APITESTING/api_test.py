import pytest
import requests

BASE_URL = "http://localhost:5000/activities"

def test_get_all():
    r = requests.get(BASE_URL)
    print(r.json())
    assert r.status_code == 201
    assert isinstance(r.json(), list)

def test_post_activity():
    payload = {"id": 3, "title": "New Activity", "completed": True}
    r = requests.post(BASE_URL, json=payload)
    print(r.json())
    test_get_all()
    assert r.status_code == 201
    assert r.json()["title"] == "New Activity"

def test_get_by_id():
    r = requests.get(f"{BASE_URL}/1")
    print(r.json())
    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_put_activity():
    payload = {"title": "Updated Activity"}
    r = requests.put(f"{BASE_URL}/1", json=payload)
    print(r.json())
    test_get_all()
    assert r.status_code == 200
    assert r.json()["title"] == "Updated Activity"

def test_delete_activity():
    r = requests.delete(f"{BASE_URL}/2")
    print(r.json())
    test_get_all()
    assert r.status_code == 200
    assert r.json()["deleted"] is True
