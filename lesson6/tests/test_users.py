from http import HTTPStatus
import pytest
from httpx import request

from lesson6.clients.users.private_users_client import PrivateUsersClient
from lesson6.clients.users.public_users_client import PublicUsersClient
from lesson6.clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from lesson6.pydantic_create_user import CreateUserResponseSchema
from lesson6.tools.assertions.schema import validate_json_schema
from lesson6.tools.assertions.base import assert_status_code
from lesson6.tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)
    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_users_client, function_user):
    response = private_users_client.get_user_me_api()
    assert_status_code(response.status_code, HTTPStatus.OK)
    response_data = GetUserResponseSchema.model_validate_json(response.text)
    assert_get_user_response(response_data, function_user.response)
    validate_json_schema(response.json(), response_data.model_json_schema())
