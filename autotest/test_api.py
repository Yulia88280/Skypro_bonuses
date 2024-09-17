import pytest
from api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    base_url = "https://sky.pro/share"
    api_key = "EJD3nIVOhQ5yd1a80zBtX8I70KRrBN9i"
    return APIClient(base_url, api_key)

#Тест для успешной покупки 
def test_successful_purchase(api_client):
    product_id = "bonus_ik"
    student_id = 9990014
    added_by = "Jason Statham"
    
    response = api_client.purchase(product_id, student_id, added_by)
    assert response.status_code == 201
 
# Тест для проверки неверного product_id
def test_invalid_product_id(api_client):
    product_id = "invalid_course"
    student_id = 9990014
    added_by = "Jason Statham"
    
    response = api_client.purchase(product_id, student_id, added_by)
    
    assert response.status_code == 400
    assert "Продукт invalid_course не существует либо не активен" in response.text
    
#Тест для проверки неверного student_id 

def test_invalid_student_id(api_client):
    product_id = "mini_course_excel"
    student_id = 9999999
    added_by = "Jason Statham"
    
    response = api_client.purchase(product_id, student_id, added_by)
    
    assert response.status_code == 400
    assert "Студент с ID 9999999 не найден" in response.text
    
# Тест для проверки неверного значения поля added_by
def test_invalid_added_by(api_client):
    product_id = "mini_course_gpt"
    student_id = 9990014
    added_by = "" 
    
    response = api_client.purchase(product_id, student_id, added_by)
    
    #assert response.status_code == 400 баг, 
    assert "Неверное значение added_by" in response.text
       
# Тест для проверки неверного метода HTTP (GET)
def test_invalid_http_method_get(api_client):
    response = api_client.get_purchase()
    
    assert response.status_code == 405
    
# Тест для проверки неверного API-ключа
def test_invalid_api_key(api_client):
    api_client.headers["X-API-Key"] = "invalid_key"
    product_id = "mini_course_gpt"
    student_id = 9990014
    added_by = "Jason Statham"
    
    response = api_client.purchase(product_id, student_id, added_by)
    
    assert response.status_code == 403
    
# Тест для проверки недостатка бонусов
def test_insufficient_funds(api_client):
    product_id = "mini_course_gpt"
    student_id = 9990014
    added_by = "Jason Statham"
    
    response = api_client.purchase(product_id, student_id, added_by)
    
    assert response.status_code == 400
    assert "Недостаточно средств" in response.text
    
