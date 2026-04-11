from http import HTTPStatus
import pytest
import allure
from lesson6.clients.users.private_users_client import PrivateUsersClient
from lesson6.clients.users.public_users_client import PublicUsersClient
from lesson6.clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from lesson6.pydantic_create_user import CreateUserResponseSchema
from lesson6.tools.assertions.schema import validate_json_schema
from lesson6.tools.assertions.base import assert_status_code
from lesson6.tools.assertions.users import assert_create_user_response, assert_get_user_response
from lesson6.fixtures.users import UserFixture
from lesson6.tools.fakers import fake
from lesson6.tools.allure.tags import AllureTag
from lesson6.tools.allure.epics import AllureEpic
from lesson6.tools.allure.stories import AllureStory
from lesson6.tools.allure.features import AllureFeature
from allure_commons.types import Severity




@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.USERS)
class TestUsers:
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    @allure.title("Create user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get user me")
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_user_me(
            self,
            function_user: UserFixture,
            private_users_client: PrivateUsersClient
    ):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validate_json_schema(response.json(), response_data.model_json_schema())