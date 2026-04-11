from http import HTTPStatus
import pytest
from lesson6.clients.authentication.authentication_client import AuthenticationClient
from lesson6.clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
import allure
from lesson6.fixtures.users import UserFixture
from lesson6.tools.assertions.authentication import assert_login_response
from lesson6.tools.assertions.base import assert_status_code
from lesson6.tools.assertions.schema import validate_json_schema
from lesson6.tools.allure.tags import AllureTag
from lesson6.tools.allure.epics import AllureEpic
from lesson6.tools.allure.stories import AllureStory
from lesson6.tools.allure.features import AllureFeature
from allure_commons.types import Severity




@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.title("Login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.LOGIN)
    def test_login(
            self,
            function_user: UserFixture,
            authentication_client: AuthenticationClient
    ):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())