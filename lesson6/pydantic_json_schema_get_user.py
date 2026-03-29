from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from lesson6.clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from lesson6.tools.fakers import fake
from tools.assertions.schema import validate_json_schema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# Проходим аутентификацию
login_payload = {
    "email": create_user_request.email,
    "password": create_user_request.password
}
user_schema = AuthenticationUserSchema(**login_payload)
login_response = get_private_users_client(user=user_schema)
#Используем залогиненный клиент, выполняем запрос на получение данных о созданном пользователе
get_user_response = login_response.get_user_api(user_id=create_user_response.user.id)

#Получаем JSON схему из модели ответа
get_user_response_schema = GetUserResponseSchema.model_json_schema()
# Проверяем, что JSON ответ от API соответствует ожидаемой JSON схеме
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)