'''
This file contains unit tests for the main file.
'''
import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_get_word_of_the_day():
    response = client.get("/word-of-the-day/2022-01-01")
    assert response.status_code == 200
    data = response.json()
    assert "word" in data
    assert "definition" in data
    assert "examples" in data
def test_get_word_of_the_day_invalid_date():
    response = client.get("/word-of-the-day/invalid-date")
    assert response.status_code == 400
    data = response.json()
    assert "error" in data