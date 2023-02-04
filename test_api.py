import requests
import pytest
import os
from contextlib import nullcontext as does_not_raise
from poly_data_api_requests import get_headers


BASE_URL = 'http://localhost:8000/api/'


@pytest.mark.parametrize("username, password, status_code",
                         [("test", "1234", 200), ("test", "389239032", 401)],
                         ids=['correct credentials return status code 200',
                              'wrong credentials return status code 401'])
def test_get_headers(username, password, status_code):
    url = os.path.join(BASE_URL, 'auth')
    access_info = {"username": username, "password": password}
    response = requests.post(url, json=access_info)
    assert response.status_code == status_code


def test_get_list_of_data_poly():
    headers = get_headers()
    url = os.path.join(BASE_URL, 'poly')
    response = requests.get(url, headers=headers)
    response_body = response.json()
    assert response.status_code == 200
    assert type(response.json()) == list


@pytest.mark.parametrize("key, value, value_type, status_code",
                         [("key1", "val1", "str", 200),
                          ("key1", 3, "int", 200),
                          ("key2", 3, "str", 400)],
                         ids=['add new objuct in the correct format and value type',
                              'add new objuct in the correct format and value type',
                              'add new objuct in the correct format but wrong value type'])
def test_add_object_to_list_of_data_poly(key, value, value_type, status_code):
    headers = get_headers()
    url = os.path.join(BASE_URL, 'poly')
    parameters = {"data": [{"key": key, "val": value, "valType": value_type}]}
    response = requests.post(url, headers=headers, json=parameters)
    assert response.status_code == status_code
    assert response.headers["Content-Type"] == "application/json"
    assert type(value).__name__ == value_type


@pytest.mark.parametrize("object_id", [1])
def test_get_poly_data_by_object_id(object_id):
    url = os.path.join(BASE_URL, f'poly/?object_id={str(object_id)}')
    headers = get_headers()
    response = requests.get(url, headers=headers)
    response_body = response.json()
    assert response.status_code == 200
    assert len(response_body) == 1


@pytest.mark.parametrize("object_id", [1])
def test_delete_poly_data_by_object_id(object_id):
    url = os.path.join(BASE_URL, f'poly/?object_id={str(object_id)}')
    headers = get_headers()
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200
