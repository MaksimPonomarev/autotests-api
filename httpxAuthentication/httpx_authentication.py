import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

token = login_response_data["token"]["accessToken"]
headers = {"Authorization": f"Bearer {token}"}
user_response = httpx.get("http://localhost:8000/api/v1/users/me",  headers=headers)
user_data = user_response.json()
print("User response:", user_data)
print("Status Code:", user_response.status_code)
