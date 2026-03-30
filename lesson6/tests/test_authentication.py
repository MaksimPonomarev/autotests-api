from http import HTTPStatus

from lesson6.clients.authentication.authentication_client import get_authentication_client
from lesson6.clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from lesson6.clients.users.public_users_client import get_public_users_client
from lesson6.pydantic_create_user import CreateUserRequestSchema
from lesson6.tools.assertions.assert_login_response import assert_login_response
from lesson6.tools.assertions.base import assert_status_code
from lesson6.tools.assertions.schema import validate_json_schema


def test_login():
    public_users_client = get_public_users_client()
    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request)

    auth_client = get_authentication_client()
    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )

    login_response = auth_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())